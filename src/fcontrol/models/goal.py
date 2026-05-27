from dataclasses import dataclass
import datetime

from fcontrol.models import Pocket


@dataclass
class Goal:
    name: str
    target_amount: float
    pocket: Pocket
    current_amount: float = 0.0
    target_date: datetime.date | None = None
    description: str = ""
    id: int | None = None

    @property
    def progress_percentage(self) -> float:
        if self.target_amount == 0:
            return 0.0
        return int((self.current_amount / self.target_amount) * 100)


class GoalRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self) -> list[Goal]:
        rows = self.db.fetch_all("""
            SELECT g.id, g.name, g.target_amount, g.current_amount, g.target_date, g.description,
                   p.id as pocket_id, p.name as pocket_name, p.currency as pocket_currency
            FROM goals g
            JOIN pockets p ON g.pocket_id = p.id
            ORDER BY g.id DESC
            """)
        goals = []
        for r in rows:
            pocket = Pocket(
                id=r["pocket_id"], name=r["pocket_name"], currency=r["pocket_currency"]
            )
            goal = Goal(
                id=r["id"],
                name=r["name"],
                target_amount=r["target_amount"],
                current_amount=r["current_amount"],
                target_date=(
                    datetime.datetime.strptime(r["target_date"], "%Y-%m-%d").date()
                    if r["target_date"]
                    else None
                ),
                description=r["description"],
                pocket=pocket,
            )
            goals.append(goal)
        return goals

    def insert(self, goal: Goal) -> Goal:
        goal.id = self.db.execute(
            """
            INSERT INTO goals (name, target_amount, current_amount, target_date, description, pocket_id)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                goal.name,
                goal.target_amount,
                goal.current_amount,
                goal.target_date.isoformat() if goal.target_date else None,
                goal.description,
                goal.pocket.id,
            ),
        )
        return goal

    def update(self, goal: Goal) -> None:
        self.db.execute(
            """
            UPDATE goals
            SET name = ?, target_amount = ?, current_amount = ?, target_date = ?, description = ?, pocket_id = ?
            WHERE id = ?
            """,
            (
                goal.name,
                goal.target_amount,
                goal.current_amount,
                goal.target_date.isoformat() if goal.target_date else None,
                goal.description,
                goal.pocket.id,
                goal.id,
            ),
        )

    def get_by_id(self, goal_id: int) -> "Goal | None":
        row = self.db.fetch_one(
            """
            SELECT g.id, g.name, g.target_amount, g.current_amount, g.target_date, g.description,
                   p.id as pocket_id, p.name as pocket_name, p.currency as pocket_currency
            FROM goals g
            JOIN pockets p ON g.pocket_id = p.id
            WHERE g.id = ?
            """,
            (goal_id,),
        )
        if not row:
            return None
        pocket = Pocket(
            id=row["pocket_id"],
            name=row["pocket_name"],
            currency=row["pocket_currency"],
        )
        return Goal(
            id=row["id"],
            name=row["name"],
            target_amount=row["target_amount"],
            current_amount=row["current_amount"],
            target_date=(
                datetime.datetime.strptime(row["target_date"], "%Y-%m-%d").date()
                if row["target_date"]
                else None
            ),
            description=row["description"],
            pocket=pocket,
        )

    def delete(self, goal_id: int) -> None:
        self.db.execute("DELETE FROM goals WHERE id = ?", (goal_id,))
