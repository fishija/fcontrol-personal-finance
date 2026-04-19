from PySide6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Signal

from fcontrol.ui.qt_generated.pockets_widget import Ui_PocketsWidget
from fcontrol.models import Pocket
from fcontrol.config import CURRENCIES


class PocketsWidget(Ui_PocketsWidget, QWidget):
    add_request = Signal(str, float, str)  # pocket name, balance, currency
    edit_request = Signal(int)  # pocket id
    delete_request = Signal(int)  # pocket id

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._setup_inputs()
        self._setup_table()
        self._connect_signals()

        # Disable delete and edit buttons until any pocket is selected
        self.deleteButton.setEnabled(False)
        self.editButton.setEnabled(False)

    def _setup_inputs(self):
        self.nameInput.setPlaceholderText("Pocket Name")

        self.balanceInput.setMinimum(0)
        self.balanceInput.setMaximum(1_000_000_000)
        self.balanceInput.setDecimals(2)
        self.balanceInput.setValue(0.00)

        self.currencySelect.addItems(CURRENCIES)

    def _setup_table(self):
        self.pocketsTable.setColumnCount(3)
        self.pocketsTable.setHorizontalHeaderLabels(["Name", "Balance", "Currency"])

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

    def _on_table_selection_changed(self):
        selected_items = self.pocketsTable.selectedItems()
        self.deleteButton.setEnabled(bool(selected_items))
        self.editButton.setEnabled(bool(selected_items))

    def _get_selected_pocket_id(self) -> int | None:
        selected_items = self.pocketsTable.selectedItems()
        if not selected_items:
            return None
        return selected_items[0].data(Qt.ItemDataRole.UserRole)

    def _ask_for_confirmation(self, message: str) -> bool:
        reply = QMessageBox.question(
            self,
            "Confirm Action",
            message,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        return reply == QMessageBox.StandardButton.Yes

    def _set_style_invalid(self, widget, is_invalid: bool):
        if is_invalid:
            widget.setStyleSheet("border: 1px solid red;")
        else:
            widget.setStyleSheet("")

    def _on_add_clicked(self):
        name = self.nameInput.text().strip()
        balance = self.balanceInput.value()
        currency = self.currencySelect.currentText()

        # perform input validation
        if not name:
            self._set_style_invalid(self.nameInput, True)
            return
        else:
            self._set_style_invalid(self.nameInput, False)

        self.add_request.emit(name, balance, currency)

    def _on_delete_clicked(self):
        pocket_id = self._get_selected_pocket_id()
        if pocket_id is not None:
            confirmation = self._ask_for_confirmation(
                "Are you sure you want to delete the selected pocket?"
            )
            if not confirmation:
                return

            self.delete_request.emit(pocket_id)

    def _on_edit_clicked(self):
        pocket_id = self._get_selected_pocket_id()
        if pocket_id is not None:
            self.edit_request.emit(pocket_id)

    def _on_double_clicked(self):
        self._on_edit_clicked()

    def populate_table(self, pockets: list[Pocket]):
        self.pocketsTable.setRowCount(0)
        for pocket in pockets:
            row = self.pocketsTable.rowCount()
            self.pocketsTable.insertRow(row)

            name_item = QTableWidgetItem(pocket.name)
            name_item.setData(Qt.ItemDataRole.UserRole, pocket.id)

            self.pocketsTable.setItem(row, 0, name_item)
            self.pocketsTable.setItem(row, 1, QTableWidgetItem(f"{pocket.balance:.2f}"))
            self.pocketsTable.setItem(row, 2, QTableWidgetItem(pocket.currency))
