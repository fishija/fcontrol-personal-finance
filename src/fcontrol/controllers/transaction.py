from PySide6.QtWidgets import QListWidget, QListWidgetItem
from PySide6.QtCore import QObject

from fcontrol.ui import TransactionsWidget
from fcontrol.services import TransactionService


class TransactionController(QObject):
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

    def refresh(self):
        transactions = self.service.get_transactions()
        self.view.populate_list(transactions)
