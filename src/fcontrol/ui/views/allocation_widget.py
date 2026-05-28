from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QComboBox,
    QSizePolicy,
)
from PySide6.QtCore import Signal, Qt

from fcontrol.ui.views.base import BaseWidget, LabelState
from fcontrol.ui.qt_generated.allocation_widget import Ui_AllocationWidget
from fcontrol.models import (
    Pocket,
    Goal,
    AllocationRule,
    AllocationType,
    AllocationResult,
    TransactionCategory,
)
from fcontrol.config import CURRENCIES


class AllocationWidget(Ui_AllocationWidget, BaseWidget):
    add_request = Signal(
        object, object, str, float, int
    )  # pocket_id (or None), goal_id (or None), allocation type, value, position
    delete_request = Signal(int)  # rule id
    edit_request = Signal(int)  # rule id
    move_up_request = Signal(int)  # rule id
    move_down_request = Signal(int)  # rule id
    allocate_request = Signal()
    income_changed = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._setup_inputs()
        self._setup_table()
        self._connect_signals()

        self._set_initial_state()

    def _setup_inputs(self):
        self.incomeInput.setMinimum(0)
        self.incomeInput.setMaximum(1_000_000_000)
        self.incomeInput.setDecimals(2)

        self.ruleValueInput.setMinimum(0)
        self.ruleValueInput.setMaximum(1_000_000_000)
        self.ruleValueInput.setDecimals(2)

        self.currencySelect.addItems(CURRENCIES)
        self.allocationTypeSelect.addItems(
            ["Select"] + [atype.value for atype in AllocationType]
        )

        # Set default state to disabled
        self.deleteButton.setEnabled(False)
        self.editButton.setEnabled(False)
        self.upButton.setEnabled(False)
        self.downButton.setEnabled(False)

    def _setup_table(self):
        self.rulesTable.setColumnCount(4)
        self.rulesTable.setHorizontalHeaderLabels(
            ["Target", "Rule", "To allocate", "New balance"]
        )

        self.rulesTable.itemDoubleClicked.connect(self._on_double_clicked)

        self.rulesTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.rulesTable.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.rulesTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

    def _connect_signals(self):
        self.incomeInput.valueChanged.connect(self._on_income_changed)
        self.currencySelect.currentTextChanged.connect(self._on_currency_changed)

        self.rulesTable.itemSelectionChanged.connect(self._on_table_selection_changed)

        self.addButton.clicked.connect(self._on_add_clicked)
        self.deleteButton.clicked.connect(self._on_delete_clicked)
        self.editButton.clicked.connect(self._on_edit_clicked)
        self.upButton.clicked.connect(self._on_move_up_clicked)
        self.downButton.clicked.connect(self._on_move_down_clicked)

        self.allocateButton.clicked.connect(self._on_allocate_clicked)

        # Exclusive selection: pocket vs goal
        self.pocketSelect.currentIndexChanged.connect(self._on_pocket_changed)
        self.goalSelect.currentIndexChanged.connect(self._on_goal_changed)

    def _on_pocket_changed(self):
        """When a pocket is selected, disable goal selection."""
        if self.pocketSelect.currentData() is not None:
            self.goalSelect.setEnabled(False)
        else:
            self.goalSelect.setEnabled(True)

    def _on_goal_changed(self):
        """When a goal is selected, disable pocket selection."""
        if self.goalSelect.currentData() is not None:
            self.pocketSelect.setEnabled(False)
        else:
            self.pocketSelect.setEnabled(True)

    def _set_initial_state(self):
        # self.infoLabel.setText("")
        self.pocketSelect.setCurrentIndex(0)
        self.pocketSelect.setEnabled(True)
        self.goalSelect.setCurrentIndex(0)
        self.goalSelect.setEnabled(True)
        self.allocationTypeSelect.setCurrentIndex(0)
        self.ruleValueInput.setValue(0.00)
        self.rulesTable.clearSelection()

    def _on_income_changed(self):
        self.income_changed.emit()

    def _on_currency_changed(self):
        self.income_changed.emit()

    def _on_table_selection_changed(self):
        selected_items = self.rulesTable.selectedItems()

        has_selection = bool(selected_items)
        self.deleteButton.setEnabled(has_selection)
        self.editButton.setEnabled(has_selection)
        self.upButton.setEnabled(has_selection)
        self.downButton.setEnabled(has_selection)

    def _on_add_clicked(self):
        pocket_id = self.pocketSelect.currentData()
        goal_id = self.goalSelect.currentData()
        allocation_type = self.allocationTypeSelect.currentText()
        value = self.ruleValueInput.value()

        # Basic validation
        if pocket_id is None and goal_id is None:
            self._set_label(
                self.infoLabel,
                "Please select a pocket or a goal for the allocation rule.",
                LabelState.ERROR,
            )
            return
        elif allocation_type == "Select":
            self._set_label(
                self.infoLabel, "Please select an allocation type.", LabelState.ERROR
            )
            return
        elif value <= 0:
            self._set_label(
                self.infoLabel,
                "Please enter a value greater than zero for the rule.",
                LabelState.ERROR,
            )
            return
        else:
            self._set_label(self.infoLabel, "")

        self.add_request.emit(
            pocket_id, goal_id, allocation_type, value, self.rulesTable.rowCount()
        )

    def _on_delete_clicked(self):
        rule_id = self.get_selected_row_id(self.rulesTable)
        if rule_id is not None:
            confirmation = self.ask_for_confirmation(
                "Are you sure you want to delete this rule?"
            )
            if confirmation:
                self.delete_request.emit(rule_id)

    def _on_edit_clicked(self):
        rule_id = self.get_selected_row_id(self.rulesTable)
        if rule_id is not None:
            self.edit_request.emit(rule_id)

    def _on_double_clicked(self):
        self._on_edit_clicked()

    def _on_move_up_clicked(self):
        rule_id = self.get_selected_row_id(self.rulesTable)
        if rule_id is not None:
            self.move_up_request.emit(rule_id)

    def _on_move_down_clicked(self):
        rule_id = self.get_selected_row_id(self.rulesTable)
        if rule_id is not None:
            self.move_down_request.emit(rule_id)

    def _on_allocate_clicked(self):
        self.allocate_request.emit()

    def get_income_data(self) -> tuple[float, str]:
        return self.incomeInput.value(), self.currencySelect.currentText()

    def get_selected_category_id(self) -> int | None:
        category_id = self.incomeCategorySelect.currentData()
        return category_id

    def set_info_message(self, message: str, state: LabelState = LabelState.DEFAULT):
        self._set_label(self.infoLabel, message, state=state)

    def clear_new_rule_inputs(self):
        self.pocketSelect.setCurrentIndex(0)
        self.pocketSelect.setEnabled(True)
        self.goalSelect.setCurrentIndex(0)
        self.goalSelect.setEnabled(True)
        self.allocationTypeSelect.setCurrentIndex(0)
        self.ruleValueInput.setValue(0.00)

    def show_allocation_success_dialog(self, message: str):
        QMessageBox.information(self, "Allocation Successful", message)

    def refresh(self):
        # Clear selection and reset inputs when refreshing
        self._set_initial_state()

    def populate_pockets(self, pockets: list[Pocket]):
        self.pocketSelect.clear()

        self.pocketSelect.addItem("Select Pocket", None)
        for pocket in pockets:
            self.pocketSelect.addItem(f"{pocket.name} ({pocket.currency})", pocket.id)

    def populate_goals(self, goals: list[Goal]):
        self.goalSelect.clear()

        self.goalSelect.addItem("Select Goal", None)
        for goal in goals:
            self.goalSelect.addItem(f"{goal.name} ({goal.pocket.currency})", goal.id)

    def populate_income_categories(self, categories: list[TransactionCategory]):
        self.incomeCategorySelect.clear()
        self.incomeCategorySelect.addItem("Select", None)
        for category in categories:
            self.incomeCategorySelect.addItem(category.name, category.id)

    def populate_rules(self, rules: list[AllocationRule]):
        # get selected row id before repopulating
        selected_rule_id = self.get_selected_row_id(self.rulesTable)
        income_currency = self.currencySelect.currentText()

        self.rulesTable.setRowCount(0)
        for rule in rules:
            row = self.rulesTable.rowCount()
            self.rulesTable.insertRow(row)

            rule_item = QTableWidgetItem(rule.get_short_name(income_currency))
            rule_item.setData(Qt.ItemDataRole.UserRole, rule.id)

            self.rulesTable.setItem(
                row,
                0,
                QTableWidgetItem(rule.get_target_display()),
            )
            self.rulesTable.setItem(row, 1, rule_item)
            self.rulesTable.setItem(row, 2, QTableWidgetItem(""))  # allocated amount
            self.rulesTable.setItem(row, 3, QTableWidgetItem(""))  # before
            self.rulesTable.setItem(row, 4, QTableWidgetItem(""))  # after

            # restore selection
            if selected_rule_id is not None and rule.id == selected_rule_id:
                self.rulesTable.selectRow(row)

    def display_calculation_results(self, results: list[AllocationResult]):
        income_currency = self.currencySelect.currentText()

        for row, result in enumerate(results):
            self.rulesTable.setItem(
                row,
                2,
                QTableWidgetItem(
                    f"{result.allocated_in_income_currency:.2f} {income_currency}"
                ),
            )

            new_balance = result.new_balance_in_pocket_currency
            new_balance_str = (
                f"{int(new_balance)}"
                if new_balance.is_integer()
                else f"{new_balance:.2f}"
            )
            self.rulesTable.setItem(
                row,
                3,
                QTableWidgetItem(
                    f"{new_balance_str} {result.rule.target_pocket.currency}"
                ),
            )
