from PySide6.QtWidgets import QListWidget, QListWidgetItem
from PySide6.QtCore import Qt

from fcontrol.ui.views.base import BaseWidget
from fcontrol.ui.qt_generated.transactions_widget import Ui_TransactionsWidget
from fcontrol.models import Transaction, TransactionType


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
            item = QListWidgetItem(transaction.summary_long)
            # set color based on transaction type
            if transaction.transaction_type == TransactionType.INCOME:
                item.setForeground(Qt.GlobalColor.green)

            self.transactionsList.addItem(item)
