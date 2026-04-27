from PySide6.QtCore import QObject, Signal

from fcontrol.models import Transaction
from fcontrol.ui import TransactionsWidget
from fcontrol.services import TransactionService
from typing import Protocol


class ApplyTransactionsCallback(Protocol):
    def __call__(self, success: bool, message: str) -> None: ...


class TransactionController(QObject):
    transactions_applied = Signal()
    allocation_transactions_applied = Signal()

    def __init__(self, view: TransactionsWidget, service: TransactionService):
        super().__init__()
        self.view = view
        self.service = service

        self.refresh()

    def _on_add(self, amount: float, date: str, category: str, description: str):
        error = self.service.add_transaction(amount, date, category, description)
        if error:
            print(error)
            return

        self.refresh()

    def apply_transactions(
        self,
        transactions: list[Transaction],
        callback: ApplyTransactionsCallback | None = None,
    ):
        try:
            for transaction in transactions:
                self.service.apply_transaction(transaction)
        except Exception as e:
            if callback:
                callback(False, str(e))
            return
        self.refresh()
        self.transactions_applied.emit()
        if callback:
            callback(
                True,
                f"Transaction{'' if len(transactions) == 1 else 's'} applied successfully.",
            )

    def refresh(self):
        transactions = self.service.get_transactions()
        self.view.populate_list(transactions)
