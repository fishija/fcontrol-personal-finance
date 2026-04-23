from fcontrol.models.allocation import AllocationRule, AllocationResult, AllocationType


class AllocationService:
    def __init__(self, currency_converter):
        self.currency_converter = currency_converter
        self.calculated_results = []

    def calculate(
        self,
        rules: list[AllocationRule],
        pocket_balances: dict[int, float],
        income_value: float,
        income_currency: str,
    ) -> list[AllocationResult]:
        results = []
        income_left = income_value

        for rule in rules:
            allocated_pocket, allocated_income = rule.calculate_allocation(
                income_value,
                income_left,
                income_currency,
                pocket_balances[rule.pocket.id],
                self.currency_converter,
            )
            income_left -= allocated_income

            pocket_balances[rule.pocket.id] += allocated_pocket
            results.append(
                AllocationResult(
                    rule=rule,
                    allocated_in_pocket_currency=allocated_pocket,
                    allocated_in_income_currency=allocated_income,
                    new_balance_in_pocket_currency=pocket_balances[rule.pocket.id],
                    income_left_after_allocation=income_left,
                )
            )

        self.calculated_results = results
        return results
