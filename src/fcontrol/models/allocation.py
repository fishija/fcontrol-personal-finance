from __future__ import annotations

from dataclasses import dataclass
import enum

from fcontrol.models.pocket import Pocket, PocketRepository
from fcontrol.models.goal import Goal, GoalRepository
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
    allocation_type: AllocationType
    value: float
    pocket: Pocket | None = None
    goal: Goal | None = None
    position: int = 0
    id: int | None = None

    def __post_init__(self):
        if not self.pocket and not self.goal:
            raise ValueError("AllocationRule must have either a pocket or a goal.")

    @property
    def target_pocket(self) -> Pocket:
        """The pocket that receives the allocation (either direct or via goal)."""
        if self.pocket:
            return self.pocket
        return self.goal.pocket

    def get_short_name(self, income_currency: str) -> str:
        if self.allocation_type == AllocationType.AMOUNT:
            return f"{self.value:.2f} {income_currency} fixed"
        elif self.allocation_type == AllocationType.PERCENTAGE:
            return f"{self.value:.1f}% of income"
        elif self.allocation_type == AllocationType.TARGET_BALANCE:
            return f"Target: {self.value:.2f} {self.target_pocket.currency}"
        else:
            return "Unknown"

    def get_target_display(self) -> str:
        """Display string for the allocation target (pocket or goal)."""
        if self.goal:
            return f"[Goal] {self.goal.name}"
        return str(self.pocket)


class AllocationRepository:
    def __init__(
        self,
        db: DatabaseManager,
        pocket_repository: PocketRepository,
        goal_repository: GoalRepository | None = None,
    ):
        self.db = db
        self.pocket_repository = pocket_repository
        self.goal_repository = goal_repository

    def _build_rule(self, row) -> AllocationRule:
        pocket = None
        goal = None
        if row["pocket_id"]:
            pocket = self.pocket_repository.get_by_id(row["pocket_id"])
        if row["goal_id"] and self.goal_repository:
            goal = self.goal_repository.get_by_id(row["goal_id"])
        return AllocationRule(
            pocket=pocket,
            goal=goal,
            allocation_type=AllocationType(row["allocation_type"]),
            value=row["value"],
            position=row["position"],
            id=row["id"],
        )

    def get_all(self) -> list[AllocationRule]:
        rows = self.db.fetch_all(
            "SELECT id, pocket_id, goal_id, allocation_type, value, position FROM allocation_rules ORDER BY position"
        )
        return [self._build_rule(r) for r in rows]

    def get_by_id(self, rule_id: int) -> AllocationRule | None:
        row = self.db.fetch_one(
            "SELECT id, pocket_id, goal_id, allocation_type, value, position FROM allocation_rules WHERE id = ?",
            (rule_id,),
        )
        if row:
            return self._build_rule(row)
        return None

    def get_by_position(self, position: int) -> AllocationRule | None:
        row = self.db.fetch_one(
            "SELECT id, pocket_id, goal_id, allocation_type, value, position FROM allocation_rules WHERE position = ?",
            (position,),
        )
        if row:
            return self._build_rule(row)
        return None

    def insert(self, rule: AllocationRule) -> AllocationRule:
        rule.id = self.db.execute(
            "INSERT INTO allocation_rules (pocket_id, goal_id, allocation_type, value, position) VALUES (?, ?, ?, ?, ?)",
            (
                rule.pocket.id if rule.pocket else None,
                rule.goal.id if rule.goal else None,
                rule.allocation_type.value,
                rule.value,
                rule.position,
            ),
        )
        return rule

    def update(self, rule: AllocationRule) -> None:
        self.db.execute(
            "UPDATE allocation_rules SET pocket_id = ?, goal_id = ?, allocation_type = ?, value = ?, position = ? WHERE id = ?",
            (
                rule.pocket.id if rule.pocket else None,
                rule.goal.id if rule.goal else None,
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
