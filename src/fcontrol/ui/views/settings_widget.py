from PySide6.QtCore import Signal

from fcontrol.ui.views.base import BaseWidget, LabelState
from fcontrol.ui.qt_generated.settings_widget import Ui_SettingsWidget
from fcontrol.config import CURRENCIES


class SettingsWidget(Ui_SettingsWidget, BaseWidget):
    currency_save_requested = Signal(str, str)  # old_currency, new_currency

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._current_currency = ""
        self._setup_inputs()
        self._connect_signals()

    def _setup_inputs(self):
        self.currencySelect.addItems(CURRENCIES)
        self.saveButton.setEnabled(False)
        self.warningLabel.setVisible(False)

    def _connect_signals(self):
        self.currencySelect.currentTextChanged.connect(
            self._on_currency_selection_changed
        )
        self.saveButton.clicked.connect(self._on_save_clicked)

    def _on_currency_selection_changed(self, currency: str):
        changed = currency != self._current_currency
        self.saveButton.setEnabled(changed)
        self.warningLabel.setVisible(changed)

    def _on_save_clicked(self):
        new_currency = self.currencySelect.currentText()
        if new_currency != self._current_currency:
            self.currency_save_requested.emit(self._current_currency, new_currency)

    def set_current_currency(self, currency: str):
        self._current_currency = currency
        self.currencySelect.blockSignals(True)
        self.currencySelect.setCurrentText(currency)
        self.currencySelect.blockSignals(False)
        self.saveButton.setEnabled(False)
        self.warningLabel.setVisible(False)

    def set_info_message(self, message: str, state: LabelState = LabelState.DEFAULT):
        self._set_label(self.infoLabel, message, state=state)

    def refresh(self):
        pass
