from dataclasses import dataclass
import enum

from fcontrol.models.pocket import Pocket, PocketRepository
from fcontrol.db_manager import DatabaseManager


class AllocationType(enum.Enum):
    AMOUNT = r"amount of income"
    PERCENTAGE = r"% of income"
    TARGET_BALANCE = r"target balance of pocket"


@dataclass
class AllocationResult:
    rule: "AllocationRule"
    allocated_in_pocket_currency: float
    allocated_in_income_currency: float
    new_balance_in_pocket_currency: float
    income_left_after_allocation: float | None = None


# TODO: add possibility to instead of value, give "all remaining from income"
@dataclass
class AllocationRule:
    pocket: Pocket
    allocation_type: AllocationType
    value: float
    position: int = 0
    id: int | None = None

    def get_short_name(self, income_currency: str) -> str:
        if self.allocation_type == AllocationType.AMOUNT:
            return f"{self.value:.2f} {income_currency} fixed"
        elif self.allocation_type == AllocationType.PERCENTAGE:
            return f"{self.value:.1f}% of income"
        elif self.allocation_type == AllocationType.TARGET_BALANCE:
            return f"Target: {self.value:.2f} {self.pocket.currency}"
        else:
            return "Unknown"

    def calculate_allocation(
        self,
        income: float,
        income_left: float,
        income_currency: str,
        current_pocket_balance: float,
        currency_converter,
    ) -> tuple[float, float]:
        """Return allocated amount in pocket currency and in income currency"""

        def convert_to_pocket_currency(amount: float) -> float:
            if income_currency != self.pocket.currency:
                return currency_converter.convert(
                    amount, income_currency, self.pocket.currency
                )
            return amount

        def convert_to_income_currency(amount: float) -> float:
            if self.pocket.currency != income_currency:
                return currency_converter.convert(
                    amount, self.pocket.currency, income_currency
                )
            return amount

        income_in_pocket_currency = convert_to_pocket_currency(income)
        income_left_in_pocket_currency = convert_to_pocket_currency(income_left)
        value_in_pocket_currency = convert_to_pocket_currency(self.value)

        if self.allocation_type == AllocationType.AMOUNT:
            allocated_in_pocket_currency = min(
                income_left_in_pocket_currency, value_in_pocket_currency
            )
            allocated_in_income_currency = min(income_left, self.value)
            return allocated_in_pocket_currency, allocated_in_income_currency

        elif self.allocation_type == AllocationType.PERCENTAGE:
            allocated_in_pocket_currency = min(
                income_in_pocket_currency * (self.value / 100),
                income_left_in_pocket_currency,
            )
            allocated_in_income_currency = min(income * (self.value / 100), income_left)
            return allocated_in_pocket_currency, allocated_in_income_currency

        elif self.allocation_type == AllocationType.TARGET_BALANCE:
            current_balance = current_pocket_balance
            if current_balance >= self.value:
                return 0.0, 0.0

            needed_in_pocket_currency = self.value - current_balance
            allocated_in_pocket_currency = min(
                income_left_in_pocket_currency, needed_in_pocket_currency
            )
            allocated_in_income_currency = convert_to_income_currency(
                allocated_in_pocket_currency
            )

            return allocated_in_pocket_currency, allocated_in_income_currency
        else:
            raise ValueError("Invalid allocation type")


class AllocationRepository:
    def __init__(self, db: DatabaseManager, pocket_repository: PocketRepository):
        self.db = db
        self.pocket_repository = pocket_repository

    def get_all(self) -> list[AllocationRule]:
        rows = self.db.fetch_all(
            "SELECT id, pocket_id, allocation_type, value, position FROM allocation_rules ORDER BY position"
        )
        return [
            AllocationRule(
                pocket=self.pocket_repository.get_by_id(r["pocket_id"]),
                allocation_type=AllocationType(r["allocation_type"]),
                value=r["value"],
                position=r["position"],
                id=r["id"],
            )
            for r in rows
        ]

    def get_by_id(self, rule_id: int) -> AllocationRule | None:
        row = self.db.fetch_one(
            "SELECT id, pocket_id, allocation_type, value, position FROM allocation_rules WHERE id = ?",
            (rule_id,),
        )
        if row:
            return AllocationRule(
                pocket=self.pocket_repository.get_by_id(row["pocket_id"]),
                allocation_type=AllocationType(row["allocation_type"]),
                value=row["value"],
                position=row["position"],
                id=row["id"],
            )
        return None

    def get_by_position(self, position: int) -> AllocationRule | None:
        row = self.db.fetch_one(
            "SELECT id, pocket_id, allocation_type, value, position FROM allocation_rules WHERE position = ?",
            (position,),
        )
        if row:
            return AllocationRule(
                pocket=self.pocket_repository.get_by_id(row["pocket_id"]),
                allocation_type=AllocationType(row["allocation_type"]),
                value=row["value"],
                position=row["position"],
                id=row["id"],
            )
        return None

    def insert(self, rule: AllocationRule) -> AllocationRule:
        rule.id = self.db.execute(
            "INSERT INTO allocation_rules (pocket_id, allocation_type, value, position) VALUES (?, ?, ?, ?)",
            (
                rule.pocket.id,
                rule.allocation_type.value,
                rule.value,
                rule.position,
            ),
        )
        return rule

    def update(self, rule: AllocationRule) -> None:
        self.db.execute(
            "UPDATE allocation_rules SET pocket_id = ?, allocation_type = ?, value = ?, position = ? WHERE id = ?",
            (
                rule.pocket.id,
                rule.allocation_type.value,
                rule.value,
                rule.position,
                rule.id,
            ),
        )

    def delete(self, rule_id: int) -> None:
        self.db.execute("DELETE FROM allocation_rules WHERE id = ?", (rule_id,))

    def count(self) -> int:
        row = self.db.fetch_one("SELECT COUNT(*) as count FROM allocation_rules")
        return row["count"] if row else 0
