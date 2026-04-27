from PySide6.QtWidgets import QListWidget, QListWidgetItem
from PySide6.QtCore import Qt, Signal

from fcontrol.ui.views.base import BaseWidget, LabelState
from fcontrol.ui.qt_generated.transactions_widget import Ui_TransactionsWidget
from fcontrol.models import Transaction, TransactionType, TransactionCategory


class TransactionsWidget(Ui_TransactionsWidget, BaseWidget):
    add_category_request = Signal(str)  # category_name
    delete_category_request = Signal(int)  # category_id

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._setup_lists()
        self._connect_signals()

        self._set_initial_state()

    def _setup_lists(self):
        self.transactionsList.setSelectionMode(QListWidget.SelectionMode.NoSelection)
        self.transactionsList.setEditTriggers(QListWidget.EditTrigger.NoEditTriggers)

        self.categoriesList.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        self.categoriesList.setEditTriggers(QListWidget.EditTrigger.NoEditTriggers)

    def _connect_signals(self):
        self.addButton.clicked.connect(self._on_add)
        self.deleteButton.clicked.connect(self._on_delete)

    def _set_initial_state(self):
        self.infoLabel.setText("")
        self.transactionsList.clear()
        self.categoriesList.clear()

    def _on_add(self):
        name_input = self.nameInput.text().strip()
        if not name_input:
            self.set_info_message(
                "Category name cannot be empty", state=LabelState.ERROR
            )
            return
        self.add_category_request.emit(name_input)

    def _on_delete(self):
        category_id = self.get_selected_row_id(self.categoriesList)
        if category_id is None:
            self.set_info_message(
                "Please select a category to delete", state=LabelState.ERROR
            )
            return
        self.delete_category_request.emit(category_id)

    def set_info_message(self, message: str, state: LabelState = LabelState.DEFAULT):
        self._set_label(self.infoLabel, message, state=state)

    def clear_add_category_input(self):
        self.nameInput.clear()

    def populate_transactions_list(self, transactions: list[Transaction]):
        self.transactionsList.clear()
        for transaction in transactions:
            item = QListWidgetItem(transaction.summary_long)
            # set color based on transaction type
            if transaction.transaction_type == TransactionType.INCOME:
                item.setForeground(Qt.GlobalColor.green)

            self.transactionsList.addItem(item)

    def populate_categories_list(self, categories: list[TransactionCategory]):
        self.categoriesList.clear()
        for category in categories:
            item = QListWidgetItem(category.name)
            item.setData(Qt.ItemDataRole.UserRole, category.id)
            self.categoriesList.addItem(item)
