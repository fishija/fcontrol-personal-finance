from PySide6.QtCore import QObject

from fcontrol.config import DEFAULT_CURRENCY
from fcontrol.ui.views.base import LabelState
from fcontrol.ui.views.net_worth_widget import NetWorthWidget
from fcontrol.ui.views.net_worth_edit_dialog import NetWorthEditDialog
from fcontrol.services.net_worth import NetWorthService


class NetWorthController(QObject):
    def __init__(self, view: NetWorthWidget, service: NetWorthService):
        super().__init__()
        self.view = view
        self.service = service

        self._connect_signals()
        self.refresh()

    def _connect_signals(self):
        self.view.take_snapshot_request.connect(self._on_take_snapshot)
        self.view.edit_request.connect(self._on_edit)
        self.view.delete_request.connect(self._on_delete)

    def _on_take_snapshot(self, note: str):
        try:
            snapshot = self.service.take_snapshot(note)
            self.view.set_info_message(
                f"Snapshot taken: {snapshot.amount:.2f} {DEFAULT_CURRENCY}",
                LabelState.SUCCESS,
            )
            self.view.noteInput.clear()
            self.refresh()
        except Exception as e:
            self.view.set_info_message(str(e), LabelState.ERROR)

    def _on_edit(self, snapshot_id: int):
        snapshots = self.service.get_snapshots()
        snapshot = next((s for s in snapshots if s.id == snapshot_id), None)
        if not snapshot:
            return

        dialog = NetWorthEditDialog(snapshot)
        if not dialog.exec():
            return

        values = dialog.get_values()
        try:
            self.service.update_snapshot(
                snapshot_id, values["amount"], values["date"], values["note"]
            )
            self.view.set_info_message("Snapshot updated.", LabelState.SUCCESS)
            self.refresh()
        except ValueError as e:
            self.view.set_info_message(str(e), LabelState.ERROR)

    def _on_delete(self, snapshot_id: int):
        self.service.delete_snapshot(snapshot_id)
        self.view.set_info_message("Snapshot deleted.", LabelState.SUCCESS)
        self.refresh()

    def refresh(self):
        snapshots = self.service.get_snapshots()
        self.view.populate_table(snapshots)
        self.view.populate_chart(snapshots)
