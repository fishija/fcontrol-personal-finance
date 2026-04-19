from dataclasses import dataclass
from fcontrol.db_manager import DatabaseManager


@dataclass
class Pocket:
    name: str
    balance: float
    currency: str
    id: int | None = None


class PocketRepository:
    def __init__(self, db: DatabaseManager):
        self.db = db

    def get_all(self) -> list[Pocket]:
        rows = self.db.fetch_all("SELECT id, name, balance, currency FROM pockets")
        print(type(rows[0]))
        return [
            Pocket(
                id=r["id"], name=r["name"], balance=r["balance"], currency=r["currency"]
            )
            for r in rows
        ]

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
