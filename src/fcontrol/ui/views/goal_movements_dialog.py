import datetime

from PySide6.QtCore import QDate, Signal

from fcontrol.ui.views.base import BaseDialog
from fcontrol.ui.qt_generated.goal_movements_dialog import (
    Ui_GoalMovementsDialog,
)


class GoalMovementsDialog(Ui_GoalMovementsDialog, BaseDialog):
    add_contribution_request = Signal(float, datetime.date, str)  # amount, date, note
    add_withdrawal_request = Signal(float, datetime.date, str)  # amount, date, note
    delete_movement_request = Signal(int)  # contribution_id

    def __init__(
        self, goal, contributions, pocket_balance, available_balance, parent=None
    ):
        super().__init__(parent)
        self.setupUi(self)

        self._setup_inputs()
        self._connect_signals()

        self.populate(goal, contributions, pocket_balance, available_balance)

    def _setup_inputs(self):
        self.amountInput.setMinimum(0.01)
        self.amountInput.setMaximum(1_000_000_000)
        self.amountInput.setDecimals(2)
        self.amountInput.setValue(0.01)

        self.dateInput.setDate(QDate.currentDate())

        self.movementsList.setSelectionMode(
            self.movementsList.SelectionMode.SingleSelection
        )

        self.removeButton.setEnabled(False)

    def _connect_signals(self):
        self.movementsList.itemSelectionChanged.connect(self._on_list_selection_changed)
        self.addButton.clicked.connect(self._on_add_clicked)
        self.removeButton.clicked.connect(self._on_remove_clicked)
        self.closeButton.clicked.connect(self.accept)

    def _on_list_selection_changed(self):
        has_selection = bool(self.movementsList.selectedItems())
        self.removeButton.setEnabled(has_selection)

    def _on_add_clicked(self):
        amount = self.amountInput.value()
        date = self.dateInput.date().toPython()
        note = self.noteInput.text().strip()

        if amount <= 0:
            return

        if self.withdrawalRadio.isChecked():
            self.add_withdrawal_request.emit(amount, date, note)
        else:
            self.add_contribution_request.emit(amount, date, note)

        self.noteInput.clear()
        self.amountInput.setValue(0.01)
        self.dateInput.setDate(QDate.currentDate())

    def _on_remove_clicked(self):
        contribution_id = self.get_selected_row_id(self.movementsList)
        if contribution_id is None:
            return

        confirmation = self.ask_for_confirmation(
            "Are you sure you want to remove this movement?"
        )
        if not confirmation:
            return

        self.delete_movement_request.emit(contribution_id)

    def populate(self, goal, contributions, pocket_balance, available_balance):
        self.infoLabel.setText(
            f"{goal.name} — Saved: {goal.current_amount:.2f} / {goal.target_amount:.2f}"
            f" ({goal.progress_percentage}%)"
        )
        self.pocketBalanceLabel.setText(
            f"Pocket balance: {pocket_balance:.2f} {goal.pocket.currency}"
        )
        self.availableBalanceLabel.setText(
            f"Available for contribution: {available_balance:.2f} {goal.pocket.currency}"
        )
        self.movementsList.clear()
        for c in contributions:
            if c.amount >= 0:
                type_prefix = "+"
            else:
                type_prefix = ""
            note_part = f" — {c.note}" if c.note else ""
            item_text = f"{c.date.strftime('%Y-%m-%d')}  |  {type_prefix}{c.amount:.2f}{note_part}"
            item = self.create_list_item(item_text, data=c.id)
            self.movementsList.addItem(item)
