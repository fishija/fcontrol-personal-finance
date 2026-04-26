from dataclasses import dataclass
from fcontrol.db_manager import DatabaseManager


@dataclass
class Pocket:
    name: str
    balance: float
    currency: str
    id: int | None = None
    # TODO: (idea) add "type" field to distinguish between cash, card, investment accounts, etc.

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
        rows = self.db.fetch_all("SELECT id, name, balance, currency FROM pockets")
        return [
            Pocket(
                id=r["id"], name=r["name"], balance=r["balance"], currency=r["currency"]
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
