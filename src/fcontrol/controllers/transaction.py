from PySide6.QtCore import QObject, Signal

from fcontrol.models import Transaction
from fcontrol.ui import TransactionsWidget
from fcontrol.services import TransactionService
from typing import Protocol

from fcontrol.ui.views.base import LabelState


class ApplyTransactionsCallback(Protocol):
    def __call__(self, success: bool, message: str) -> None: ...


class TransactionController(QObject):
    transactions_applied = Signal()
    category_repo_changed = Signal()

    def __init__(self, view: TransactionsWidget, service: TransactionService):
        super().__init__()
        self.view = view
        self.service = service

        self._connect_signals()
        self.refresh()

    def _connect_signals(self):
        self.view.add_category_request.connect(self._on_add_category)
        self.view.delete_category_request.connect(self._on_delete_category)

    def _on_add_category(self, category_name: str):
        try:
            self.service.add_category(category_name)
            self.refresh()
            self.view.clear_add_category_input()
        except Exception as e:
            print(str(e))
            self.view.set_info_message(str(e), state=LabelState.ERROR)
        self.category_repo_changed.emit()

    def _on_delete_category(self, category_id: int):
        try:
            self.service.delete_category(category_id)
            self.refresh()
        except Exception as e:
            self.view.set_info_message(str(e), state=LabelState.ERROR)
        self.category_repo_changed.emit()

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
        categories = self.service.get_categories()

        self.view.populate_transactions_list(transactions)
        self.view.populate_categories_list(categories)
