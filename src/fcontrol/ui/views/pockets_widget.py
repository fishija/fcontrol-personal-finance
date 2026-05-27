from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt, Signal

from fcontrol.ui.views.base import BaseWidget, LabelState
from fcontrol.ui.qt_generated.pockets_widget import Ui_PocketsWidget
from fcontrol.models import Pocket
from fcontrol.config import CURRENCIES


class PocketsWidget(Ui_PocketsWidget, BaseWidget):
    add_request = Signal(str, float, str)  # pocket name, balance, currency
    edit_request = Signal(int)  # pocket id
    delete_request = Signal(int)  # pocket id

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._setup_inputs()
        self._setup_table()
        self._connect_signals()

        self._set_initial_state()

    def _setup_inputs(self):
        self.nameInput.setPlaceholderText("Pocket Name")

        self.balanceInput.setMinimum(-1_000_000_000)
        self.balanceInput.setMaximum(1_000_000_000)
        self.balanceInput.setDecimals(2)
        self.balanceInput.setValue(0.00)

        self.currencySelect.addItems(CURRENCIES)

        # Set default state to disabled
        self.deleteButton.setEnabled(False)
        self.editButton.setEnabled(False)

    def _setup_table(self):
        self.pocketsTable.setColumnCount(4)
        self.pocketsTable.setHorizontalHeaderLabels(
            ["Name", "Balance", "Reserved", "Currency"]
        )

        self.pocketsTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.pocketsTable.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )
        self.pocketsTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

    def _connect_signals(self):
        self.pocketsTable.itemSelectionChanged.connect(self._on_table_selection_changed)
        self.pocketsTable.itemDoubleClicked.connect(self._on_double_clicked)

        self.addButton.clicked.connect(self._on_add_clicked)
        self.editButton.clicked.connect(self._on_edit_clicked)
        self.deleteButton.clicked.connect(self._on_delete_clicked)

    def _set_initial_state(self):
        self.infoLabel.setText("")
        self.pocketsTable.clearSelection()
        self.nameInput.clear()
        self.balanceInput.setValue(0.00)
        self.currencySelect.setCurrentIndex(0)

    def _on_table_selection_changed(self):
        selected_items = self.pocketsTable.selectedItems()
        has_selection = bool(selected_items)
        self.deleteButton.setEnabled(has_selection)
        self.editButton.setEnabled(has_selection)

    def _on_add_clicked(self):
        name = self.nameInput.text().strip()
        balance = self.balanceInput.value()
        currency = self.currencySelect.currentText()

        # Basic validation
        if not name:
            self.set_info_message(
                "Please enter a name for the pocket.", state=LabelState.ERROR
            )
            return
        else:
            self.set_info_message("")

        self.add_request.emit(name, balance, currency)

    def _on_delete_clicked(self):
        pocket_id = self.get_selected_row_id(self.pocketsTable)
        if pocket_id is not None:
            confirmation = self.ask_for_confirmation(
                "Are you sure you want to delete the selected pocket?"
            )
            if not confirmation:
                return

            self.delete_request.emit(pocket_id)

    def _on_edit_clicked(self):
        pocket_id = self.get_selected_row_id(self.pocketsTable)
        if pocket_id is not None:
            self.edit_request.emit(pocket_id)

    def _on_double_clicked(self):
        self._on_edit_clicked()

    def clear_new_pocket_inputs(self):
        self.nameInput.clear()
        self.balanceInput.setValue(0.00)
        self.currencySelect.setCurrentIndex(0)

    def set_info_message(self, message: str, state: LabelState = LabelState.DEFAULT):
        self._set_label(self.infoLabel, message, state=state)

    def refresh(self):
        # Clear selection and reset inputs when refreshing
        self._set_initial_state()

    def populate_table(self, pockets: list[Pocket]):
        self.pocketsTable.setRowCount(0)
        for pocket in pockets:
            row = self.pocketsTable.rowCount()
            self.pocketsTable.insertRow(row)

            name_item = QTableWidgetItem(pocket.name)
            name_item.setData(Qt.ItemDataRole.UserRole, pocket.id)

            reserved = pocket.reserved_amount
            available = pocket.balance - reserved
            reserved_text = f"{reserved:.2f}" if reserved > 0 else "—"

            balance_text = f"{pocket.balance:.2f}"
            if available != pocket.balance:
                balance_text += f" ({available:.2f} available)"

            self.pocketsTable.setItem(row, 0, name_item)
            self.pocketsTable.setItem(
                row,
                1,
                QTableWidgetItem(balance_text),
            )
            self.pocketsTable.setItem(row, 2, QTableWidgetItem(reserved_text))
            self.pocketsTable.setItem(row, 3, QTableWidgetItem(pocket.currency))
