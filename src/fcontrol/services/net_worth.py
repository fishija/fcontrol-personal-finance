from datetime import date

from currency_converter import CurrencyConverter

from fcontrol.models import PocketRepository
from fcontrol.models.net_worth import NetWorthSnapshot, NetWorthSnapshotRepository
from fcontrol.settings import AppSettings


class NetWorthService:
    def __init__(
        self,
        snapshot_repository: NetWorthSnapshotRepository,
        pocket_repository: PocketRepository,
        currency_converter: CurrencyConverter,
        settings: AppSettings,
    ):
        self.snapshot_repository = snapshot_repository
        self.pocket_repository = pocket_repository
        self.currency_converter = currency_converter
        self.settings = settings

    def get_default_currency(self) -> str:
        return self.settings.get_default_currency()

    def get_snapshots(self) -> list[NetWorthSnapshot]:
        return self.snapshot_repository.get_all()

    def take_snapshot(self, note: str = "") -> NetWorthSnapshot:
        currency = self.settings.get_default_currency()
        pockets = self.pocket_repository.get_all()

        total = 0.0
        for pocket in pockets:
            if pocket.currency == currency:
                total += pocket.balance
            else:
                converted = self.currency_converter.convert(
                    pocket.balance, pocket.currency, currency
                )
                total += converted

        snapshot = NetWorthSnapshot(
            amount=round(total, 2),
            date=date.today().isoformat(),
            note=note,
        )
        return self.snapshot_repository.insert(snapshot)

    def recalculate_snapshots(self, old_currency: str, new_currency: str) -> None:
        """Convert all snapshot amounts from old_currency to new_currency using historical rates."""
        snapshots = self.snapshot_repository.get_all()
        for snapshot in snapshots:
            snapshot_date = date.fromisoformat(snapshot.date)
            converted = self.currency_converter.convert(
                snapshot.amount, old_currency, new_currency, date=snapshot_date
            )
            snapshot.amount = round(converted, 2)
            self.snapshot_repository.update(snapshot)

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
