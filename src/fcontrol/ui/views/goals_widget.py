from PySide6.QtCore import Qt, QDate, Signal

from fcontrol.ui.views.base import BaseWidget
from fcontrol.ui.qt_generated.goals_widget import Ui_GoalsWidget


class GoalsWidget(Ui_GoalsWidget, BaseWidget):
    add_request = Signal(
        str, int, float, object, str
    )  # name, pocket_id, target_amount, target_date (date | None), description
    edit_request = Signal(int)  # goal_id
    delete_request = Signal(int)  # goal_id
    contributions_request = Signal(int)  # goal_id

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._setup_inputs()
        self._connect_signals()

        self._set_initial_state()

    def _set_target_date_enabled(self, enabled: bool):
        self.targetDateInput.setDisabled(not enabled)
        self.targetDateLabel.setDisabled(not enabled)

    def _setup_inputs(self):
        self.targetAmountInput.setMinimum(0)
        self.targetAmountInput.setMaximum(1_000_000_000)
        self.targetAmountInput.setDecimals(2)
        self.targetAmountInput.setValue(0.00)

        self.targetDateInput.setMinimumDate(QDate.currentDate())
        self.targetDateInput.setDate(QDate.currentDate())
        self._set_target_date_enabled(False)

        self.deleteButton.setEnabled(False)
        self.editButton.setEnabled(False)
        self.contributionsButton.setEnabled(False)

    def _connect_signals(self):
        self.setTargetDateInput.stateChanged.connect(self._on_set_target_date_changed)
        self.listWidget.itemSelectionChanged.connect(self._on_list_selection_changed)
        self.listWidget.itemDoubleClicked.connect(self._on_contributions_clicked)
        self.addButton.clicked.connect(self._on_add_clicked)
        self.editButton.clicked.connect(self._on_edit_clicked)
        self.deleteButton.clicked.connect(self._on_delete_clicked)
        self.contributionsButton.clicked.connect(self._on_contributions_clicked)

    def _set_initial_state(self):
        self.listWidget.clearSelection()
        self.nameInput.clear()
        self.targetAmountInput.setValue(0.00)
        self.setTargetDateInput.setChecked(False)
        self.targetDateInput.setDate(QDate.currentDate())
        self.descriptionInput.clear()

    def _on_set_target_date_changed(self, state):
        enabled = Qt.CheckState(state) == Qt.CheckState.Checked
        self._set_target_date_enabled(enabled)

    def _on_list_selection_changed(self):
        has_selection = bool(self.listWidget.selectedItems())
        self.deleteButton.setEnabled(has_selection)
        self.editButton.setEnabled(has_selection)
        self.contributionsButton.setEnabled(has_selection)

    def _on_add_clicked(self):
        name = self.nameInput.text().strip()
        pocket_id = self.pocketSelect.currentData()
        target_amount = self.targetAmountInput.value()
        target_date = (
            self.targetDateInput.date().toPython()
            if self.setTargetDateInput.isChecked()
            else None
        )
        description = self.descriptionInput.toPlainText().strip()

        if not name:
            print("Goal name cannot be empty.")
            return

        if pocket_id is None:
            print("Please select a pocket for the goal.")
            return

        self.add_request.emit(name, pocket_id, target_amount, target_date, description)

    def _on_edit_clicked(self):
        goal_id = self.get_selected_row_id(self.listWidget)
        if goal_id is not None:
            self.edit_request.emit(goal_id)

    def _on_delete_clicked(self):
        goal_id = self.get_selected_row_id(self.listWidget)
        if goal_id is not None:
            confirmation = self.ask_for_confirmation(
                "Are you sure you want to delete the selected goal?"
            )
            if not confirmation:
                return

            self.delete_request.emit(goal_id)

    def _on_contributions_clicked(self):
        goal_id = self.get_selected_row_id(self.listWidget)
        if goal_id is not None:
            self.contributions_request.emit(goal_id)

    def populate_pocket_select(self, pockets):
        self.pocketSelect.clear()
        for pocket in pockets:
            self.pocketSelect.addItem(f"{pocket.name} ({pocket.currency})", pocket.id)

    def populate_goal_list(self, goals):
        self.listWidget.clear()
        for goal in goals:
            item_text = (
                f"{goal.name}"
                f"  |  Pocket: {goal.pocket.name} ({goal.pocket.currency})"
                f"  |  {goal.current_amount:.2f} / {goal.target_amount:.2f} {goal.pocket.currency}"
                f"  ({goal.progress_percentage}%)"
            )
            if goal.target_date:
                item_text += f"  |  by {goal.target_date.strftime('%d.%m.%Y')}"
            item = self.create_list_item(item_text, data=goal.id)
            self.listWidget.addItem(item)

    def refresh(self):
        self._set_initial_state()
