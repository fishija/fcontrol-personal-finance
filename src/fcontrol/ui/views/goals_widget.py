from PySide6.QtCore import Qt, QDate

from fcontrol.ui.views.base import BaseWidget
from fcontrol.ui.qt_generated.goals_widget import Ui_GoalsWidget


class GoalsWidget(Ui_GoalsWidget, BaseWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._setup_inputs()
        self._connect_signals()

    def _set_target_date_enabled(self, enabled):
        self.targetDateInput.setDisabled(not enabled)
        self.targetDateLabel.setDisabled(not enabled)

    def _setup_inputs(self):
        self.targetAmountInput.setMinimum(0)
        self.targetAmountInput.setDecimals(2)
        self.targetAmountInput.setValue(0.00)

        self.targetDateInput.setMinimumDate(QDate.currentDate())
        self.targetDateInput.setDate(QDate.currentDate())
        self._set_target_date_enabled(False)

    def _on_set_target_date_changed(self, state):
        enabled = Qt.CheckState(state) == Qt.CheckState.Checked
        self._set_target_date_enabled(enabled)

    def _connect_signals(self):
        self.setTargetDateInput.stateChanged.connect(self._on_set_target_date_changed)
