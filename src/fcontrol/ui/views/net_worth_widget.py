from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout
from PySide6.QtCore import Qt, Signal
from PySide6.QtWebEngineWidgets import QWebEngineView

import plotly.graph_objects as go

from fcontrol.ui.views.base import BaseWidget, LabelState
from fcontrol.ui.qt_generated.net_worth_widget import Ui_NetWorthWidget
from fcontrol.models.net_worth import NetWorthSnapshot


class NetWorthWidget(Ui_NetWorthWidget, BaseWidget):
    take_snapshot_request = Signal(str)  # note
    edit_request = Signal(int)  # snapshot id
    delete_request = Signal(int)  # snapshot id

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._setup_inputs()
        self._setup_table()
        self._setup_chart()
        self._connect_signals()
        self._set_initial_state()

    def _setup_inputs(self):
        # Hide the currency selector (will be used in future settings module)
        self.currencyLabel.hide()
        self.currencySelect.hide()
        self.deleteButton.setEnabled(False)
        self.editButton.setEnabled(False)

    def _setup_table(self):
        self.snapshotsTable.setColumnCount(3)
        self.snapshotsTable.setHorizontalHeaderLabels(["Date", "Amount", "Note"])
        self.snapshotsTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.snapshotsTable.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )
        self.snapshotsTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

    def _setup_chart(self):
        layout = QVBoxLayout(self.chartContainer)
        layout.setContentsMargins(0, 0, 0, 0)

        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

    def _connect_signals(self):
        self.snapshotsTable.itemSelectionChanged.connect(
            self._on_table_selection_changed
        )
        self.snapshotsTable.itemDoubleClicked.connect(self._on_double_clicked)
        self.takeSnapshotButton.clicked.connect(self._on_take_snapshot_clicked)
        self.editButton.clicked.connect(self._on_edit_clicked)
        self.deleteButton.clicked.connect(self._on_delete_clicked)

    def _set_initial_state(self):
        self.infoLabel.setText("")
        self.snapshotsTable.clearSelection()
        self.noteInput.clear()

    def _on_table_selection_changed(self):
        selected_items = self.snapshotsTable.selectedItems()
        has_selection = bool(selected_items)
        self.deleteButton.setEnabled(has_selection)
        self.editButton.setEnabled(has_selection)

    def _on_take_snapshot_clicked(self):
        note = self.noteInput.text().strip()
        self.take_snapshot_request.emit(note)

    def _on_edit_clicked(self):
        snapshot_id = self.get_selected_row_id(self.snapshotsTable)
        if snapshot_id is not None:
            self.edit_request.emit(snapshot_id)

    def _on_double_clicked(self):
        self._on_edit_clicked()

    def _on_delete_clicked(self):
        snapshot_id = self.get_selected_row_id(self.snapshotsTable)
        if snapshot_id is not None:
            confirmation = self.ask_for_confirmation(
                "Are you sure you want to delete the selected snapshot?"
            )
            if not confirmation:
                return
            self.delete_request.emit(snapshot_id)

    def set_info_message(self, message: str, state: LabelState = LabelState.DEFAULT):
        self._set_label(self.infoLabel, message, state=state)

    def refresh(self):
        self._set_initial_state()

    def populate_table(self, snapshots: list[NetWorthSnapshot]):
        self.snapshotsTable.setRowCount(0)
        for snapshot in reversed(snapshots):
            row = self.snapshotsTable.rowCount()
            self.snapshotsTable.insertRow(row)

            date_item = QTableWidgetItem(snapshot.date)
            date_item.setData(Qt.ItemDataRole.UserRole, snapshot.id)

            self.snapshotsTable.setItem(row, 0, date_item)
            self.snapshotsTable.setItem(
                row, 1, QTableWidgetItem(f"{snapshot.amount:.2f}")
            )
            self.snapshotsTable.setItem(row, 2, QTableWidgetItem(snapshot.note))

    def populate_chart(self, snapshots: list[NetWorthSnapshot], currency: str = "PLN"):
        if not snapshots:
            self.web_view.setHtml("")
            return

        dates = [s.date for s in snapshots]
        amounts = [s.amount for s in snapshots]

        fig = go.Figure(data=[go.Bar(x=dates, y=amounts, name="Net Worth")])
        fig.update_layout(
            yaxis_title=f"Net Worth ({currency})",
            margin=dict(l=50, r=20, t=20, b=40),
            plot_bgcolor="white",
            paper_bgcolor="white",
        )

        html = fig.to_html(include_plotlyjs="cdn", full_html=True)
        html = html.replace(
            "<head>",
            "<head><style>"
            "html,body{margin:0;padding:0;width:100%;height:100%;overflow:hidden;}"
            ".plotly-graph-div{width:100vw!important;height:100vh!important;}"
            "</style>",
        )
        self.web_view.setHtml(html)
