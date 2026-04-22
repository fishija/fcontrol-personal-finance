from dataclasses import dataclass
import enum

from fcontrol.models.pocket import Pocket, PocketRepository
from fcontrol.db_manager import DatabaseManager


class AllocationType(enum.Enum):
    AMOUNT = r"amount of income"
    PERCENTAGE = r"% of income"
    TARGET_BALANCE = r"target balance of pocket"


# TODO: add possibility to instead of value, give "all remaining from income"
@dataclass
class AllocationRule:
    pocket: Pocket
    allocation_type: AllocationType
    value: float
    position: int = 0
    id: int | None = None

    @property
    def short_name(self) -> str:
        if self.allocation_type == AllocationType.AMOUNT:
            return f"{self.value:.2f} {self.pocket.currency} fixed"
        elif self.allocation_type == AllocationType.PERCENTAGE:
            return f"{self.value:.1f}% of income"
        elif self.allocation_type == AllocationType.TARGET_BALANCE:
            return f"Target: {self.value:.2f} {self.pocket.currency}"
        else:
            return "Unknown"

    def calculate_allocation(self, income: float) -> float:
        if self.allocation_type == AllocationType.AMOUNT:
            return self.value
        elif self.allocation_type == AllocationType.PERCENTAGE:
            return income * (self.value / 100)
        elif self.allocation_type == AllocationType.TARGET_BALANCE:
            return max(0, self.value - self.pocket.balance)
        else:
            raise ValueError("Invalid allocation type")


class AllocationRepository:
    def __init__(self, db: DatabaseManager, pocket_repository: PocketRepository):
        self.rules: list[AllocationRule] = []
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
