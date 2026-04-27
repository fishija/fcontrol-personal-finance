from PySide6.QtCore import QObject, Signal

from fcontrol.ui.views.base import LabelState
from fcontrol.ui import PocketsWidget, PocketEditDialog
from fcontrol.services import PocketService
from fcontrol.models import Transaction


class PocketController(QObject):
    pocket_repo_changed = Signal()
    apply_transactions_requested = Signal(
        list
    )  # List of transactions to apply when adding/editing/deleting pockets

    def __init__(self, view: PocketsWidget, service: PocketService):
        super().__init__()
        self.view = view
        self.service = service

        self._connect_signals()
        self.refresh()

    def _connect_signals(self):
        self.view.add_request.connect(self._on_add)
        self.view.edit_request.connect(self._on_edit)
        self.view.delete_request.connect(self._on_delete)

    def _on_add(self, name: str, balance: float, currency: str):
        try:
            add_transaction = self.service.create_add_transaction(
                name, balance, currency
            )
        except Exception as e:
            self.view.set_info_message(
                f"Unexpected error when adding pocket: {str(e)}", LabelState.ERROR
            )
            return

        # Emit add transaction to be applied
        self.apply_transactions_requested.emit([add_transaction])

    def _on_edit(self, pocket_id: int):
        pocket = self.service.get_pocket_by_id(pocket_id)
        if not pocket:
            print(f"Pocket with ID {pocket_id} not found.")
            return

        dialog = PocketEditDialog(pocket)
        if not dialog.exec():
            return

        new_values = dialog.get_values()
        try:
            update_transaction = self.service.create_update_transaction(
                pocket,
                new_values["name"],
                new_values["balance"],
                new_values["currency"],
            )
        except Exception as e:
            self.view.set_info_message(
                f"Unexpected error when updating pocket: {str(e)}", LabelState.ERROR
            )
            return

        if update_transaction:
            self.apply_transactions_requested.emit([update_transaction])
            return

        self.refresh()
        self.pocket_repo_changed.emit()

    def _on_delete(self, pocket_id: int):
        try:
            self.service.delete_pocket(pocket_id)
        except Exception as e:
            self.view.set_info_message(
                f"Unexpected error when deleting pocket: {str(e)}", LabelState.ERROR
            )
            return

        self.refresh()
        self.pocket_repo_changed.emit()

    def refresh(self):
        pockets = self.service.get_pockets()
        self.view.populate_table(pockets)
