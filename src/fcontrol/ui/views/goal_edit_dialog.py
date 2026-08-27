import datetime

from PySide6.QtCore import QDate, Qt

from fcontrol.ui.views.base import BaseDialog
from fcontrol.ui.qt_generated.goal_edit_dialog import Ui_GoalEditDialog


class GoalEditDialog(Ui_GoalEditDialog, BaseDialog):
    def __init__(self, goal, pockets, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self._setup_inputs(pockets)
        self._populate(goal)
        self._connect_signals()

    def _setup_inputs(self, pockets):
        self.targetAmountInput.setMinimum(0)
        self.targetAmountInput.setMaximum(1_000_000_000)
        self.targetAmountInput.setDecimals(2)

        self.targetDateInput.setMinimumDate(QDate.currentDate())

        for pocket in pockets:
            self.pocketSelect.addItem(f"{pocket.name} ({pocket.currency})", pocket.id)

    def _populate(self, goal):
        self.nameInput.setText(goal.name)
        self.pocketSelect.setCurrentText(f"{goal.pocket.name} ({goal.pocket.currency})")
        self.targetAmountInput.setValue(float(goal.target_amount))
        self.descriptionInput.setPlainText(goal.description)

        if goal.target_date:
            self.setTargetDateInput.setChecked(True)
            self.targetDateInput.setDate(
                QDate(
                    goal.target_date.year, goal.target_date.month, goal.target_date.day
                )
            )
        else:
            self.setTargetDateInput.setChecked(False)
            self.targetDateInput.setDate(QDate.currentDate())
            self._set_target_date_enabled(False)

    def _set_target_date_enabled(self, enabled: bool):
        self.targetDateInput.setDisabled(not enabled)
        self.targetDateLabel.setDisabled(not enabled)

    def _on_set_target_date_changed(self, state):
        enabled = Qt.CheckState(state) == Qt.CheckState.Checked
        self._set_target_date_enabled(enabled)

    def _connect_signals(self):
        self.setTargetDateInput.stateChanged.connect(self._on_set_target_date_changed)
        self.saveButton.clicked.connect(self._on_save_clicked)
        self.cancelButton.clicked.connect(self.reject)

    def _on_save_clicked(self):
        if not self.nameInput.text().strip():
            print("Goal name cannot be empty.")
            return
        self.accept()

    def get_values(self) -> dict:
        return {
            "name": self.nameInput.text().strip(),
            "pocket_id": self.pocketSelect.currentData(),
            "target_amount": self.targetAmountInput.value(),
            "target_date": (
                self.targetDateInput.date().toPython()
                if self.setTargetDateInput.isChecked()
                else None
            ),
            "description": self.descriptionInput.toPlainText().strip(),
        }
