from dataclasses import dataclass
from decimal import Decimal

from fcontrol.db_manager import DatabaseManager


@dataclass
class NetWorthSnapshot:
    amount: Decimal
    date: str
    note: str = ""
    id: int | None = None


class NetWorthSnapshotRepository:
    def __init__(self, db: DatabaseManager):
        self.db = db

    def get_all(self) -> list[NetWorthSnapshot]:
        rows = self.db.fetch_all(
            "SELECT id, amount, date, note FROM net_worth_snapshots ORDER BY date ASC"
        )
        return [
            NetWorthSnapshot(
                id=r["id"],
                amount=Decimal(str(r["amount"])),
                date=r["date"],
                note=r["note"],
            )
            for r in rows
        ]

    def get_by_id(self, snapshot_id: int) -> NetWorthSnapshot | None:
        row = self.db.fetch_one(
            "SELECT id, amount, date, note FROM net_worth_snapshots WHERE id = ?",
            (snapshot_id,),
        )
        if row:
            return NetWorthSnapshot(
                id=row["id"],
                amount=Decimal(str(row["amount"])),
                date=row["date"],
                note=row["note"],
            )
        return None

    def insert(self, snapshot: NetWorthSnapshot) -> NetWorthSnapshot:
        snapshot.id = self.db.execute(
            "INSERT INTO net_worth_snapshots (amount, date, note) VALUES (?, ?, ?)",
            (snapshot.amount, snapshot.date, snapshot.note),
        )
        return snapshot

    def update(self, snapshot: NetWorthSnapshot) -> None:
        self.db.execute(
            "UPDATE net_worth_snapshots SET amount = ?, date = ?, note = ? WHERE id = ?",
            (snapshot.amount, snapshot.date, snapshot.note, snapshot.id),
        )

    def delete(self, snapshot_id: int) -> None:
        self.db.execute("DELETE FROM net_worth_snapshots WHERE id = ?", (snapshot_id,))
