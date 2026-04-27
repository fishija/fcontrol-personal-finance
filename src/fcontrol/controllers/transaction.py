from PySide6.QtCore import QObject, Signal

from fcontrol.models import Transaction
from fcontrol.ui import TransactionsWidget
from fcontrol.services import TransactionService


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

    def _apply_transactions(self, transactions: list[Transaction]):
        for transaction in transactions:
            self.service.apply_transaction(transaction)
        self.refresh()

    def apply_allocation_transactions(self, transactions: list[Transaction]):
        self._apply_transactions(transactions)
        self.allocation_transactions_applied.emit()

    def apply_transactions(self, transactions: list[Transaction]):
        self._apply_transactions(transactions)
        self.transactions_applied.emit()

    def refresh(self):
        transactions = self.service.get_transactions()
        self.view.populate_list(transactions)
