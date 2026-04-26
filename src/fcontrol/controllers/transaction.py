from PySide6.QtCore import QObject, Signal

from fcontrol.models import Transaction
from fcontrol.ui import TransactionsWidget
from fcontrol.services import TransactionService


class TransactionController(QObject):
    apply_allocation_transactions_success = Signal(str)  # allocation summary message

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

        # Prepare summary message for the allocation results
        if not transactions:
            return "No transactions were created during allocation."

        summary_message = "Allocation created the following transactions:\n\n"
        for t in transactions:
            summary_message += f"{t.summary_short}\n"

        self.apply_allocation_transactions_success.emit(summary_message)

    def refresh(self):
        transactions = self.service.get_transactions()
        self.view.populate_list(transactions)
