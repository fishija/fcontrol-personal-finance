from PySide6.QtWidgets import QListWidget, QListWidgetItem
from PySide6.QtCore import Qt, Signal
import datetime

from fcontrol.ui.views.base import BaseWidget, LabelState
from fcontrol.ui.qt_generated.transactions_widget import Ui_TransactionsWidget
from fcontrol.models import (
    Transaction,
    TransactionType,
    TransactionCategory,
    TransactionSource,
)


class TransactionsWidget(Ui_TransactionsWidget, BaseWidget):
    add_category_request = Signal(str)  # category_name
    delete_category_request = Signal(int)  # category_id

    add_transaction_request = Signal(
        float, int, TransactionType, TransactionSource, datetime.date, object, str
    )  # amount, pocket_id, transaction_type, source, date, category_id (int | None), description
    delete_transaction_request = Signal(int)  # transaction_id

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._set_inputs()
        self._setup_lists()
        self._connect_signals()

        self._set_initial_state()

    def _set_inputs(self):
        # Pocket and category selects will be populated dynamically
        self.transactionAmountInput.setMinimum(0)
        self.transactionAmountInput.setMaximum(1_000_000_000)
        self.transactionAmountInput.setDecimals(2)

        self.transactionDateInput.setDate(datetime.date.today())
        self.transactionDateInput.setCalendarPopup(True)

        self.transactionTypeSelect.addItems([t.value for t in TransactionType])

    def _setup_lists(self):
        self.transactionsList.setSelectionMode(
            QListWidget.SelectionMode.SingleSelection
        )
        self.transactionsList.setEditTriggers(QListWidget.EditTrigger.NoEditTriggers)

        self.categoriesList.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        self.categoriesList.setEditTriggers(QListWidget.EditTrigger.NoEditTriggers)

    def _connect_signals(self):
        self.addCategoryButton.clicked.connect(self._on_add_category)
        self.deleteCategoryButton.clicked.connect(self._on_delete_category)

        self.addTransactionButton.clicked.connect(self._on_add_transaction)
        self.deleteTransactionButton.clicked.connect(self._on_delete_transaction)

    def _set_initial_state(self):
        self.infoLabel.setText("")
        self.transactionsList.clear()
        self.categoriesList.clear()

    def _on_add_category(self):
        name_input = self.categoryNameInput.text().strip()
        if not name_input:
            self.set_info_message(
                "Category name cannot be empty", state=LabelState.ERROR
            )
            return
        self.add_category_request.emit(name_input)

    def _on_delete_category(self):
        category_id = self.get_selected_row_id(self.categoriesList)
        if category_id is None:
            self.set_info_message(
                "Please select a category to delete", state=LabelState.ERROR
            )
            return

        confirmation = self.ask_for_confirmation(
            "Are you sure you want to delete the selected category?"
        )
        if not confirmation:
            return
        self.delete_category_request.emit(category_id)

    def _on_add_transaction(self):
        amount = self.transactionAmountInput.value()
        pocket_id = self.transactionPocketSelect.currentData()
        transaction_type_str = self.transactionTypeSelect.currentText()
        transaction_type = TransactionType(transaction_type_str)
        source = TransactionSource.MANUAL
        date = self.transactionDateInput.date().toPython()
        category_id = self.transactionCategorySelect.currentData()
        description = self.transactionDescriptionInput.text().strip()

        if pocket_id is None:
            self.set_info_message(
                "Please select a pocket for the transaction", state=LabelState.ERROR
            )
            return
        elif amount <= 0:
            self.set_info_message(
                "Please enter an amount greater than zero", state=LabelState.ERROR
            )
            return

        self.add_transaction_request.emit(
            amount, pocket_id, transaction_type, source, date, category_id, description
        )

    def _on_delete_transaction(self):
        transaction_id = self.get_selected_row_id(self.transactionsList)
        if transaction_id is None:
            self.set_info_message(
                "Please select a transaction to delete", state=LabelState.ERROR
            )
            return

        confirmation = self.ask_for_confirmation(
            "Are you sure you want to delete the selected transaction?"
        )
        if not confirmation:
            return
        self.delete_transaction_request.emit(transaction_id)

    def set_info_message(self, message: str, state: LabelState = LabelState.DEFAULT):
        self._set_label(self.infoLabel, message, state=state)

    def clear_add_category_input(self):
        self.categoryNameInput.clear()

    def populate_transactions_list(self, transactions: list[Transaction]):
        self.transactionsList.clear()
        for transaction in transactions:
            item = QListWidgetItem(transaction.summary_long)
            item.setData(Qt.ItemDataRole.UserRole, transaction.id)
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

    def populate_pockets_select(self, pockets: list):
        self.transactionPocketSelect.clear()
        for pocket in pockets:
            self.transactionPocketSelect.addItem(
                f"{pocket.name} ({pocket.currency})", userData=pocket.id
            )

    def populate_category_select(self, categories: list[TransactionCategory]):
        self.transactionCategorySelect.clear()
        self.transactionCategorySelect.addItem("No category", userData=None)
        for category in categories:
            self.transactionCategorySelect.addItem(category.name, userData=category.id)
