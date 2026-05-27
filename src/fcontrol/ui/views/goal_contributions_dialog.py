import datetime

from PySide6.QtCore import QDate, Signal

from fcontrol.ui.views.base import BaseDialog
from fcontrol.ui.qt_generated.goal_contributions_dialog import (
    Ui_GoalContributionsDialog,
)


class GoalContributionsDialog(Ui_GoalContributionsDialog, BaseDialog):
    add_contribution_request = Signal(float, datetime.date, str)  # amount, date, note
    delete_contribution_request = Signal(int)  # contribution_id

    def __init__(self, goal, contributions, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self._setup_inputs()
        self._connect_signals()

        self.populate(goal, contributions)

    def _setup_inputs(self):
        self.amountInput.setMinimum(0.01)
        self.amountInput.setMaximum(1_000_000_000)
        self.amountInput.setDecimals(2)
        self.amountInput.setValue(0.01)

        self.dateInput.setDate(QDate.currentDate())

        self.contributionsList.setSelectionMode(
            self.contributionsList.SelectionMode.SingleSelection
        )

        self.removeButton.setEnabled(False)

    def _connect_signals(self):
        self.contributionsList.itemSelectionChanged.connect(
            self._on_list_selection_changed
        )
        self.addContributionButton.clicked.connect(self._on_add_clicked)
        self.removeButton.clicked.connect(self._on_remove_clicked)
        self.closeButton.clicked.connect(self.accept)

    def _on_list_selection_changed(self):
        has_selection = bool(self.contributionsList.selectedItems())
        self.removeButton.setEnabled(has_selection)

    def _on_add_clicked(self):
        amount = self.amountInput.value()
        date = self.dateInput.date().toPython()
        note = self.noteInput.text().strip()

        if amount <= 0:
            print("Contribution amount must be greater than zero.")
            return

        self.add_contribution_request.emit(amount, date, note)
        self.noteInput.clear()
        self.amountInput.setValue(0.01)
        self.dateInput.setDate(QDate.currentDate())

    def _on_remove_clicked(self):
        contribution_id = self.get_selected_row_id(self.contributionsList)
        if contribution_id is None:
            return

        confirmation = self.ask_for_confirmation(
            "Are you sure you want to remove this contribution?"
        )
        if not confirmation:
            return

        self.delete_contribution_request.emit(contribution_id)

    def populate(self, goal, contributions):
        self.infoLabel.setText(
            f"{goal.name} — Saved: {goal.current_amount:.2f} / {goal.target_amount:.2f}"
            f" ({goal.progress_percentage}%)"
        )
        self.contributionsList.clear()
        for c in contributions:
            note_part = f" — {c.note}" if c.note else ""
            item_text = f"{c.date.strftime('%Y-%m-%d')}  |  {c.amount:.2f}{note_part}"
            item = self.create_list_item(item_text, data=c.id)
            self.contributionsList.addItem(item)
