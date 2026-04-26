from fcontrol.models import (
    AllocationRule,
    AllocationResult,
    AllocationType,
    Transaction,
    TransactionType,
    PocketRepository,
    AllocationRepository,
    TransactionCategoryRepository,
)
from currency_converter import CurrencyConverter


class AllocationService:
    def __init__(
        self,
        allocation_repository: AllocationRepository,
        pocket_repository: PocketRepository,
        transaction_category_repository: TransactionCategoryRepository,
        currency_converter: CurrencyConverter,
    ):
        self.pocket_repository = pocket_repository
        self.allocation_repository = allocation_repository
        self.transaction_category_repository = transaction_category_repository
        self.currency_converter = currency_converter

        self.calculated_results = []

    def _calculate_allocation(
        self,
        rule: AllocationRule,
        income_value: float,
        income_left: float,
        income_currency: str,
        current_pocket_balance: float,
    ) -> tuple[float, float]:
        """Return allocated amount in pocket currency and in income currency"""

        def convert_to_pocket_currency(amount: float) -> float:
            if income_currency != rule.pocket.currency:
                return self.currency_converter.convert(
                    amount, income_currency, rule.pocket.currency
                )
            return amount

        def convert_to_income_currency(amount: float) -> float:
            if rule.pocket.currency != income_currency:
                return self.currency_converter.convert(
                    amount, rule.pocket.currency, income_currency
                )
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
            current_balance = current_pocket_balance
            if current_balance >= rule.value:
                return 0.0, 0.0

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

    def get_income_categories(self):
        return self.transaction_category_repository.get_all(
            transaction_type=TransactionType.INCOME
        )

    def get_allocation_rules(self):
        return self.allocation_repository.get_all()

    def validate_rule(self, allocation_type: str, value: float) -> str | None:
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
        self, income_value: float, income_currency: str, results: list[AllocationResult]
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
        self, pocket_id: int, allocation_type: str, value: float, position: int
    ) -> str | None:
        error = self.validate_rule(allocation_type, value)

        if error:
            return error

        pocket = self.pocket_repository.get_by_id(pocket_id)
        if not pocket:
            return f"Pocket with ID {pocket_id} not found."

        rule = AllocationRule(
            pocket=pocket,
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
        self, rule_id: int, pocket_id: int, allocation_type: str, value: float
    ) -> str | None:
        error = self.validate_rule(allocation_type, value)
        if error:
            return error

        rule = self.allocation_repository.get_by_id(rule_id)
        if not rule:
            raise ValueError(f"Allocation rule with ID {rule_id} not found.")

        pocket = self.pocket_repository.get_by_id(pocket_id)
        if not pocket:
            raise ValueError(f"Pocket with ID {pocket_id} not found.")

        rule.pocket = pocket
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
        self, income_value: float, income_currency: str
    ) -> list[AllocationResult]:
        results = []
        income_left = income_value

        # Fetch pockets and rules
        pockets = self.pocket_repository.get_all()
        rules = self.allocation_repository.get_all()
        pocket_balances = {pocket.id: pocket.balance for pocket in pockets}

        for rule in rules:
            pocket_id = rule.pocket.id

            allocated_pocket, allocated_income = self._calculate_allocation(
                rule,
                income_value,
                income_left,
                income_currency,
                pocket_balances[pocket_id],
            )
            income_left -= allocated_income

            pocket_balances[pocket_id] += allocated_pocket
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
        self, transaction_category_id: int
    ) -> list[Transaction]:
        transactions = []

        income_category = self.transaction_category_repository.get_by_id(
            transaction_category_id
        )

        for result in self.calculated_results:
            if result.allocated_in_pocket_currency > 0:
                transactions.append(
                    Transaction(
                        amount=round(result.allocated_in_pocket_currency, 2),
                        pocket=result.rule.pocket,
                        category=income_category,
                        description=f"Allocation to {result.rule.pocket.name}",
                    )
                )
        return transactions
