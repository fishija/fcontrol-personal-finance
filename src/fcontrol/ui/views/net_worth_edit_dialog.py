from PySide6.QtWidgets import (
    QVBoxLayout,
    QFormLayout,
    QDoubleSpinBox,
    QDateEdit,
    QLineEdit,
    QDialogButtonBox,
)
from PySide6.QtCore import QDate

from fcontrol.ui.views.base import BaseDialog
from fcontrol.models.net_worth import NetWorthSnapshot


class NetWorthEditDialog(BaseDialog):
    def __init__(self, snapshot: NetWorthSnapshot, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Snapshot")
        self._setup_ui(snapshot)

    def _setup_ui(self, snapshot: NetWorthSnapshot):
        layout = QVBoxLayout(self)
        form = QFormLayout()

        self.amountInput = QDoubleSpinBox()
        self.amountInput.setMinimum(-1_000_000_000)
        self.amountInput.setMaximum(1_000_000_000)
        self.amountInput.setDecimals(2)
        self.amountInput.setValue(snapshot.amount)
        form.addRow("Amount:", self.amountInput)

        self.dateInput = QDateEdit()
        self.dateInput.setCalendarPopup(True)
        date = QDate.fromString(snapshot.date, "yyyy-MM-dd")
        self.dateInput.setDate(date)
        form.addRow("Date:", self.dateInput)

        self.noteInput = QLineEdit()
        self.noteInput.setText(snapshot.note)
        self.noteInput.setPlaceholderText("Note (optional)")
        form.addRow("Note:", self.noteInput)

        layout.addLayout(form)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_values(self) -> dict:
        return {
            "amount": self.amountInput.value(),
            "date": self.dateInput.date().toString("yyyy-MM-dd"),
            "note": self.noteInput.text().strip(),
        }
