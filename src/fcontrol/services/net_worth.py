from datetime import date

from currency_converter import CurrencyConverter

from fcontrol.config import DEFAULT_CURRENCY
from fcontrol.models import PocketRepository
from fcontrol.models.net_worth import NetWorthSnapshot, NetWorthSnapshotRepository


class NetWorthService:
    def __init__(
        self,
        snapshot_repository: NetWorthSnapshotRepository,
        pocket_repository: PocketRepository,
        currency_converter: CurrencyConverter,
    ):
        self.snapshot_repository = snapshot_repository
        self.pocket_repository = pocket_repository
        self.currency_converter = currency_converter

    def get_snapshots(self) -> list[NetWorthSnapshot]:
        return self.snapshot_repository.get_all()

    def take_snapshot(self, note: str = "") -> NetWorthSnapshot:
        pockets = self.pocket_repository.get_all()

        total = 0.0
        for pocket in pockets:
            if pocket.currency == DEFAULT_CURRENCY:
                total += pocket.balance
            else:
                converted = self.currency_converter.convert(
                    pocket.balance, pocket.currency, DEFAULT_CURRENCY
                )
                total += converted

        snapshot = NetWorthSnapshot(
            amount=round(total, 2),
            date=date.today().isoformat(),
            note=note,
        )
        return self.snapshot_repository.insert(snapshot)

    def update_snapshot(
        self, snapshot_id: int, amount: float, snapshot_date: str, note: str
    ) -> None:
        error = self.validate_snapshot_data(amount, snapshot_date)
        if error:
            raise ValueError(error)

        snapshot = self.snapshot_repository.get_by_id(snapshot_id)
        if not snapshot:
            raise ValueError("Snapshot not found.")

        snapshot.amount = amount
        snapshot.date = snapshot_date
        snapshot.note = note
        self.snapshot_repository.update(snapshot)

    def delete_snapshot(self, snapshot_id: int) -> None:
        self.snapshot_repository.delete(snapshot_id)

    def validate_snapshot_data(self, amount: float, snapshot_date: str) -> str | None:
        if not snapshot_date.strip():
            return "Date cannot be empty."
        try:
            date.fromisoformat(snapshot_date)
        except ValueError:
            return "Invalid date format. Use YYYY-MM-DD."
        return None
