from PySide6.QtCore import QObject, Signal

from fcontrol.ui.views.base import LabelState
from fcontrol.ui import PocketsWidget, PocketEditDialog
from fcontrol.services import PocketService


class PocketController(QObject):
    pocket_repo_changed = Signal()

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
            error = self.service.add_pocket(name, balance, currency)
            if error:
                self.view.set_info_message(error, LabelState.ERROR)
                return
        except Exception as e:
            self.view.set_info_message(
                f"Unexpected error when adding pocket: {str(e)}", LabelState.ERROR
            )
            return

        self.refresh()
        self.pocket_repo_changed.emit()
        self.view.clear_new_pocket_inputs()

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
            error = self.service.update_pocket(
                pocket_id,
                new_values["name"],
                new_values["balance"],
                new_values["currency"],
            )
            if error:
                self.view.set_info_message(error, LabelState.ERROR)
                return
        except Exception as e:
            self.view.set_info_message(
                f"Unexpected error when updating pocket: {str(e)}", LabelState.ERROR
            )
            return

        self.refresh()
        self.pocket_repo_changed.emit()

    def _on_delete(self, pocket_id: int):
        try:
            error = self.service.delete_pocket(pocket_id)
            if error:
                self.view.set_info_message(error, LabelState.ERROR)
                return
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
