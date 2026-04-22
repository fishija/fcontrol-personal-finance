from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtCore import Signal, Qt

from fcontrol.ui.views.base import BaseWidget
from fcontrol.ui.qt_generated.allocation_widget import Ui_AllocationWidget
from fcontrol.models import Pocket, AllocationRule, AllocationType
from fcontrol.config import CURRENCIES


class AllocationWidget(Ui_AllocationWidget, BaseWidget):
    add_request = Signal(
        int, str, float, int
    )  # pocket id, allocation type, value, position (row in the table)
    delete_request = Signal(int)  # rule id
    edit_request = Signal(int)  # rule id
    move_up_request = Signal(int)  # rule id
    move_down_request = Signal(int)  # rule id

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
        self.rulesTable.setColumnCount(3)
        self.rulesTable.setHorizontalHeaderLabels(
            ["Pocket", "Rule", "Left to Allocate"]
        )

        self.rulesTable.itemDoubleClicked.connect(self._on_double_clicked)

        self.rulesTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.rulesTable.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.rulesTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

    def _connect_signals(self):
        self.rulesTable.itemSelectionChanged.connect(self._on_table_selection_changed)

        self.addButton.clicked.connect(self._on_add_clicked)
        self.deleteButton.clicked.connect(self._on_delete_clicked)
        self.editButton.clicked.connect(self._on_edit_clicked)
        self.upButton.clicked.connect(self._on_move_up_clicked)
        self.downButton.clicked.connect(self._on_move_down_clicked)

    def _set_initial_state(self):
        # Clear any default text in the info label
        self.infoLabel.setText("")
        self.pocketSelect.setCurrentIndex(0)
        self.allocationTypeSelect.setCurrentIndex(0)
        self.ruleValueInput.setValue(0.00)
        self.rulesTable.clearSelection()

    def _on_table_selection_changed(self):
        selected_items = self.rulesTable.selectedItems()
        has_selection = bool(selected_items)

        self.deleteButton.setEnabled(has_selection)
        self.editButton.setEnabled(has_selection)
        self.upButton.setEnabled(has_selection)
        self.downButton.setEnabled(has_selection)

    def _clear_new_rule_inputs(self):
        self.pocketSelect.setCurrentIndex(0)
        self.allocationTypeSelect.setCurrentIndex(0)
        self.ruleValueInput.setValue(0.00)

    def _on_add_clicked(self):
        pocket_id = self.pocketSelect.currentData()
        allocation_type = self.allocationTypeSelect.currentText()
        value = self.ruleValueInput.value()

        # Basic validation
        if pocket_id is None:
            self._set_label(
                self.infoLabel,
                "Please select a pocket for the allocation rule.",
                is_error=True,
            )
            return
        elif allocation_type == "Select":
            self._set_label(
                self.infoLabel, "Please select an allocation type.", is_error=True
            )
            return
        elif value <= 0:
            self._set_label(
                self.infoLabel,
                "Please enter a value greater than zero for the rule.",
                is_error=True,
            )
            return
        else:
            self._set_label(self.infoLabel, "", is_error=False)

        self.add_request.emit(
            pocket_id, allocation_type, value, self.rulesTable.rowCount()
        )
        self._clear_new_rule_inputs()

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

    def refresh(self):
        # Clear selection and reset inputs when refreshing
        self._set_initial_state()

    def populate_pockets(self, pockets: list[Pocket]):
        self.pocketSelect.clear()

        self.pocketSelect.addItem("Select", None)
        for pocket in pockets:
            self.pocketSelect.addItem(f"{pocket.name} ({pocket.currency})", pocket.id)

    def populate_rules(self, rules: list[AllocationRule]):
        # get selected row id before repopulating
        selected_rule_id = self.get_selected_row_id(self.rulesTable)

        self.rulesTable.setRowCount(0)
        for rule in rules:
            row = self.rulesTable.rowCount()
            self.rulesTable.insertRow(row)

            rule_item = QTableWidgetItem(rule.short_name)
            rule_item.setData(Qt.ItemDataRole.UserRole, rule.id)

            self.rulesTable.setItem(row, 0, QTableWidgetItem(rule.pocket.name))
            self.rulesTable.setItem(row, 1, rule_item)
            self.rulesTable.setItem(row, 2, QTableWidgetItem(""))  # left to allocate

            # restore selection
            if selected_rule_id is not None and rule.id == selected_rule_id:
                self.rulesTable.selectRow(row)
