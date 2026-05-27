from dataclasses import dataclass
from fcontrol.db_manager import DatabaseManager


@dataclass
class Pocket:
    name: str
    currency: str
    balance: float = 0.0
    id: int | None = None
    # TODO: (idea) add "type" field to distinguish between cash, card, investment accounts, etc.
    # Computed from goal_contributions — never written to the DB
    reserved_amount: float = 0.0

    def __str__(self):
        balance_str = (
            f"{int(self.balance)}"
            if self.balance.is_integer()
            else f"{self.balance:.2f}"
        )
        return f"{self.name} ({balance_str} {self.currency})"

    def __hash__(self):
        return hash(self.id)


class PocketRepository:
    def __init__(self, db: DatabaseManager):
        self.db = db

    def get_all(self) -> list[Pocket]:
        rows = self.db.fetch_all("""
            SELECT p.id, p.name, p.balance, p.currency,
                   COALESCE(SUM(gc.amount), 0) as reserved_amount
            FROM pockets p
            LEFT JOIN goals g ON g.pocket_id = p.id
            LEFT JOIN goal_contributions gc ON gc.goal_id = g.id
            GROUP BY p.id
        """)
        return [
            Pocket(
                id=r["id"],
                name=r["name"],
                balance=r["balance"],
                currency=r["currency"],
                reserved_amount=r["reserved_amount"],
            )
            for r in rows
        ]

    def get_by_id(self, pocket_id: int) -> Pocket | None:
        row = self.db.fetch_one(
            "SELECT id, name, balance, currency FROM pockets WHERE id = ?", (pocket_id,)
        )
        if row:
            return Pocket(
                id=row["id"],
                name=row["name"],
                balance=row["balance"],
                currency=row["currency"],
            )
        return None

    def insert(self, pocket: Pocket) -> Pocket:
        pocket.id = self.db.execute(
            "INSERT INTO pockets (name, balance, currency) VALUES (?, ?, ?)",
            (pocket.name, pocket.balance, pocket.currency),
        )
        return pocket

    def update(self, pocket: Pocket) -> None:
        self.db.execute(
            "UPDATE pockets SET name = ?, balance = ?, currency = ? WHERE id = ?",
            (pocket.name, pocket.balance, pocket.currency, pocket.id),
        )

    def delete(self, pocket_id: int) -> None:
        self.db.execute("DELETE FROM pockets WHERE id = ?", (pocket_id,))
