from PySide6.QtWidgets import QListWidget, QListWidgetItem

from fcontrol.ui.views.base import BaseWidget
from fcontrol.ui.qt_generated.transactions_widget import Ui_TransactionsWidget
from fcontrol.models import Transaction


class TransactionsWidget(Ui_TransactionsWidget, BaseWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._setup_list()

    def _setup_list(self):
        self.transactionsList.setSelectionMode(QListWidget.SelectionMode.NoSelection)
        self.transactionsList.setEditTriggers(QListWidget.EditTrigger.NoEditTriggers)

    def populate_list(self, transactions: list[Transaction]):
        self.transactionsList.clear()
        for transaction in transactions:
            item = QListWidgetItem(
                f"{transaction.date} - {transaction.category.name} - {transaction.amount} {transaction.currency}"
            )
            self.transactionsList.addItem(item)
