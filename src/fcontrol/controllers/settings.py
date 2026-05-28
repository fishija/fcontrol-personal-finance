from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox

from fcontrol.ui.views.base import LabelState
from fcontrol.ui.views.settings_widget import SettingsWidget
from fcontrol.services.net_worth import NetWorthService
from fcontrol.settings import AppSettings


class SettingsController(QObject):
    default_currency_changed = Signal(str)  # new currency

    def __init__(
        self,
        view: SettingsWidget,
        settings: AppSettings,
        net_worth_service: NetWorthService,
    ):
        super().__init__()
        self.view = view
        self.settings = settings
        self.net_worth_service = net_worth_service

        self._connect_signals()
        self._init_currency()

    def _connect_signals(self):
        self.view.currency_save_requested.connect(self._on_currency_save)

    def _init_currency(self):
        currency = self.settings.get_default_currency()
        self.view.set_current_currency(currency)

    def _on_currency_save(self, old_currency: str, new_currency: str):
        # Confirmation dialog
        reply = QMessageBox.warning(
            self.view,
            "Change Default Currency",
            f"Changing currency from {old_currency} to {new_currency} will "
            f"convert all Net Worth snapshots using historical exchange rates.\n\n"
            f"This may introduce small rounding differences.\n\n"
            f"Do you want to proceed?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if reply != QMessageBox.StandardButton.Yes:
            return

        try:
            self.net_worth_service.recalculate_snapshots(old_currency, new_currency)
            self.settings.set_default_currency(new_currency)
            self.view.set_current_currency(new_currency)
            self.view.set_info_message(
                f"Currency changed to {new_currency}. Snapshots recalculated.",
                LabelState.SUCCESS,
            )
            self.default_currency_changed.emit(new_currency)
        except Exception as e:
            self.view.set_info_message(
                f"Error during conversion: {e}", LabelState.ERROR
            )
