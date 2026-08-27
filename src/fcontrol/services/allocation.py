from decimal import Decimal

from fcontrol.models import (
    AllocationRule,
    AllocationResult,
    AllocationType,
    Transaction,
    TransactionType,
    TransactionSource,
    PocketRepository,
    AllocationRepository,
    TransactionCategoryRepository,
    Goal,
    GoalRepository,
    GoalContribution,
    GoalContributionRepository,
)
from currency_converter import CurrencyConverter
import datetime

_CENTS = Decimal("0.01")


class AllocationService:
    def __init__(
        self,
        allocation_repository: AllocationRepository,
        pocket_repository: PocketRepository,
        transaction_category_repository: TransactionCategoryRepository,
        currency_converter: CurrencyConverter,
        goal_repository: GoalRepository | None = None,
        goal_contribution_repository: GoalContributionRepository | None = None,
    ):
        self.pocket_repository = pocket_repository
        self.allocation_repository = allocation_repository
        self.transaction_category_repository = transaction_category_repository
        self.currency_converter = currency_converter
        self.goal_repository = goal_repository
        self.goal_contribution_repository = goal_contribution_repository

        self.calculated_results = []

    def _calculate_allocation(
        self,
        rule: AllocationRule,
        income_value: Decimal,
        income_left: Decimal,
        income_currency: str,
        current_pocket_balance: Decimal,
        current_goal_balance: Decimal = Decimal(0),
    ) -> tuple[Decimal, Decimal]:
        """Return allocated amount in pocket currency and in income currency"""
        pocket = rule.target_pocket

        def convert_to_pocket_currency(amount: Decimal) -> Decimal:
            if income_currency != pocket.currency:
                return Decimal(str(self.currency_converter.convert(
                    float(amount), income_currency, pocket.currency
                )))
            return amount

        def convert_to_income_currency(amount: Decimal) -> Decimal:
            if pocket.currency != income_currency:
                return Decimal(str(self.currency_converter.convert(
                    float(amount), pocket.currency, income_currency
                )))
            return amount

        income_in_pocket_currency = convert_to_pocket_currency(income_value)
        income_left_in_pocket_currency = convert_to_pocket_currency(income_left)
        value_in_pocket_currency = convert_to_pocket_currency(rule.value)

        if rule.allocation_type == AllocationType.AMOUNT:
            allocated_in_pocket_currency = min(
                income_left_in_pocket_currency, value_in_pocket_currency
            )
            allocated_in_income_currency = min(income_left, rule.value)
            return allocated_in_pocket_currency, allocated_in_income_currency

        elif rule.allocation_type == AllocationType.PERCENTAGE:
            allocated_in_pocket_currency = min(
                income_in_pocket_currency * (rule.value / 100),
                income_left_in_pocket_currency,
            )
            allocated_in_income_currency = min(
                income_value * (rule.value / 100), income_left
            )
            return allocated_in_pocket_currency, allocated_in_income_currency

        elif rule.allocation_type == AllocationType.TARGET_BALANCE:
            current_balance = (
                current_goal_balance
                if rule.goal is not None
                else current_pocket_balance
            )
            if current_balance >= rule.value:
                return Decimal(0), Decimal(0)

            needed_in_pocket_currency = rule.value - current_balance
            allocated_in_pocket_currency = min(
                income_left_in_pocket_currency, needed_in_pocket_currency
            )
            allocated_in_income_currency = convert_to_income_currency(
                allocated_in_pocket_currency
            )

            return allocated_in_pocket_currency, allocated_in_income_currency
        else:
            raise ValueError("Invalid allocation type")

    def _move_rule(self, rule_id: int, direction: int) -> str | None:
        rule = self.allocation_repository.get_by_id(rule_id)
        if not rule:
            raise ValueError(f"Allocation rule with ID {rule_id} not found.")

        # Check if there is a rule in the target position
        rule_to_swap = self.allocation_repository.get_by_position(
            rule.position + direction
        )
        if rule_to_swap:
            # Swap positions
            rule_to_swap.position -= direction
            self.allocation_repository.update(rule_to_swap)
            rule.position += direction
            self.allocation_repository.update(rule)
        else:
            return "Cannot move rule further in that direction."
        return None

    def get_pockets(self):
        return self.pocket_repository.get_all()

    def get_goals(self) -> list[Goal]:
        if self.goal_repository:
            return self.goal_repository.get_all()
        return []

    def get_income_categories(self):
        return self.transaction_category_repository.get_all()

    def get_allocation_rules(self):
        return self.allocation_repository.get_all()

    def validate_rule(self, allocation_type: str, value: Decimal) -> str | None:
        try:
            allocation_type_enum = AllocationType(allocation_type)
        except ValueError:
            return f"Invalid allocation type: {allocation_type}"

        if allocation_type_enum == AllocationType.AMOUNT and value < 0:
            return "Amount must be non-negative"
        elif allocation_type_enum == AllocationType.PERCENTAGE and not (
            0 <= value <= 100
        ):
            return "Percentage must be between 0 and 100"
        elif allocation_type_enum == AllocationType.TARGET_BALANCE and value < 0:
            return "Target balance must be non-negative"
        return None

    def validate_allocation_results(
        self, income_value: Decimal, income_currency: str, results: list[AllocationResult]
    ) -> str | None:
        if income_value == 0:
            return "Enter an income value to allocate."
        if not results:
            return "No allocation rules defined."

        last_result = results[-1]
        left_to_allocate = last_result.income_left_after_allocation

        if left_to_allocate > 0:
            return f"{left_to_allocate:.2f} {income_currency} left to allocate."
        return None

    def add_rule(
        self,
        pocket_id: int | None,
        goal_id: int | None,
        allocation_type: str,
        value: Decimal,
        position: int,
    ) -> str | None:
        error = self.validate_rule(allocation_type, value)

        if error:
            return error

        if not pocket_id and not goal_id:
            return "Select a pocket or a goal for the allocation rule."

        pocket = None
        goal = None

        if pocket_id:
            pocket = self.pocket_repository.get_by_id(pocket_id)
            if not pocket:
                return f"Pocket with ID {pocket_id} not found."

        if goal_id and self.goal_repository:
            goal = self.goal_repository.get_by_id(goal_id)
            if not goal:
                return f"Goal with ID {goal_id} not found."

        rule = AllocationRule(
            pocket=pocket,
            goal=goal,
            allocation_type=AllocationType(allocation_type),
            value=value,
            position=position,
        )
        self.allocation_repository.insert(rule)
        return None

    def delete_rule(self, rule_id: int) -> str | None:
        self.allocation_repository.delete(rule_id)
        return None

    def update_rule(
        self,
        rule_id: int,
        pocket_id: int | None,
        goal_id: int | None,
        allocation_type: str,
        value: Decimal,
    ) -> str | None:
        error = self.validate_rule(allocation_type, value)
        if error:
            return error

        if not pocket_id and not goal_id:
            return "Select a pocket or a goal for the allocation rule."

        rule = self.allocation_repository.get_by_id(rule_id)
        if not rule:
            raise ValueError(f"Allocation rule with ID {rule_id} not found.")

        pocket = None
        goal = None

        if pocket_id:
            pocket = self.pocket_repository.get_by_id(pocket_id)
            if not pocket:
                raise ValueError(f"Pocket with ID {pocket_id} not found.")

        if goal_id and self.goal_repository:
            goal = self.goal_repository.get_by_id(goal_id)
            if not goal:
                raise ValueError(f"Goal with ID {goal_id} not found.")

        rule.pocket = pocket
        rule.goal = goal
        rule.allocation_type = AllocationType(allocation_type)
        rule.value = value
        self.allocation_repository.update(rule)
        return None

    def move_rule_up(self, rule_id: int) -> str | None:
        return self._move_rule(rule_id, direction=-1)

    def move_rule_down(self, rule_id: int) -> str | None:
        return self._move_rule(rule_id, direction=1)

    def get_rule_by_id(self, rule_id: int) -> AllocationRule | None:
        return self.allocation_repository.get_by_id(rule_id)

    def get_rule_by_position(self, position: int) -> AllocationRule | None:
        return self.allocation_repository.get_by_position(position)

    def calculate_allocations(
        self, income_value: Decimal, income_currency: str
    ) -> list[AllocationResult]:
        results = []
        income_left = income_value

        # Fetch pockets and rules
        pockets = self.pocket_repository.get_all()
        rules = self.allocation_repository.get_all()
        pocket_balances = {pocket.id: pocket.balance for pocket in pockets}

        goals = self.goal_repository.get_all() if self.goal_repository else []
        goal_balances = {goal.id: goal.current_amount for goal in goals}

        for rule in rules:
            pocket = rule.target_pocket
            pocket_id = pocket.id
            goal_id = rule.goal.id if rule.goal else None

            allocated_pocket, allocated_income = self._calculate_allocation(
                rule,
                income_value,
                income_left,
                income_currency,
                pocket_balances.get(pocket_id, Decimal(0)),
                goal_balances.get(goal_id, Decimal(0)) if goal_id is not None else Decimal(0),
            )
            income_left -= allocated_income

            pocket_balances[pocket_id] = (
                pocket_balances.get(pocket_id, Decimal(0)) + allocated_pocket
            )
            if goal_id is not None:
                goal_balances[goal_id] = (
                    goal_balances.get(goal_id, Decimal(0)) + allocated_pocket
                )
            results.append(
                AllocationResult(
                    rule=rule,
                    allocated_in_pocket_currency=allocated_pocket,
                    allocated_in_income_currency=allocated_income,
                    new_balance_in_pocket_currency=pocket_balances[pocket_id],
                    income_left_after_allocation=income_left,
                )
            )

        self.calculated_results = results
        return results

    def create_allocation_transactions(
        self, transaction_category_id: int | None
    ) -> list[Transaction]:
        transactions = []

        if transaction_category_id is None:
            income_category = None
        else:
            income_category = self.transaction_category_repository.get_by_id(
                transaction_category_id
            )

        for result in self.calculated_results:
            if result.allocated_in_pocket_currency > 0:
                transactions.append(
                    Transaction(
                        amount=abs(result.allocated_in_pocket_currency.quantize(_CENTS)),
                        pocket=result.rule.target_pocket,
                        transaction_type=TransactionType.INCOME,
                        category=income_category,
                        source=TransactionSource.ALLOCATION,
                        description="Income allocation",
                    )
                )
        return transactions

    def create_goal_contributions(self) -> list[GoalContribution]:
        """Create goal contributions for allocation rules that target a goal."""
        contributions = []
        for result in self.calculated_results:
            if result.rule.goal and result.allocated_in_pocket_currency > 0:
                contribution = GoalContribution(
                    goal_id=result.rule.goal.id,
                    amount=result.allocated_in_pocket_currency.quantize(_CENTS),
                    date=datetime.date.today(),
                    note="Income allocation",
                )
                contributions.append(contribution)
        return contributions

    def apply_goal_contributions(self) -> None:
        """Persist goal contributions for goal-targeted allocation rules."""
        if not self.goal_contribution_repository:
            return
        contributions = self.create_goal_contributions()
        for contribution in contributions:
            self.goal_contribution_repository.insert(contribution)
