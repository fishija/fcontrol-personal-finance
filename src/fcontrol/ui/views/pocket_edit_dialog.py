from PySide6.QtWidgets import QDialog

from fcontrol.ui.qt_generated.pocket_edit_dialog import Ui_PocketEditDialog
from fcontrol.config import CURRENCIES


class PocketEditDialog(Ui_PocketEditDialog, QDialog):
    def __init__(self, pocket, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._set_inputs()
        self._populate(pocket)
        self._connect_signals()

    def _set_inputs(self):
        self.balanceInput.setMinimum(0)
        self.balanceInput.setMaximum(1_000_000_000)
        self.balanceInput.setDecimals(2)

        self.currencySelect.addItems(CURRENCIES)

    def _populate(self, pocket):
        # Populate current lineEdit fields first (left side)
        self.currentName.setText(pocket.name)
        self.currentBalance.setText(str(pocket.balance))
        self.currentCurrency.setText(pocket.currency)

        # Populate new input fields (right side) with current values as placeholders
        self.nameInput.setText(pocket.name)
        self.balanceInput.setValue(pocket.balance)
        self.currencySelect.setCurrentText(pocket.currency)

    def _set_style_invalid(self, widget, is_invalid: bool):
        if is_invalid:
            widget.setStyleSheet("border: 1px solid red;")
        else:
            widget.setStyleSheet("")

    def _connect_signals(self):
        self.saveButton.clicked.connect(self._on_save_clicked)
        self.cancelButton.clicked.connect(self.reject)

    def _on_save_clicked(self):
        # Validate inputs
        if not self.nameInput.text().strip():
            self._set_style_invalid(self.nameInput, True)
            return
        else:
            self._set_style_invalid(self.nameInput, False)

        self.accept()

    def get_values(self):
        return {
            "name": self.nameInput.text(),
            "balance": self.balanceInput.value(),
            "currency": self.currencySelect.currentText(),
        }
