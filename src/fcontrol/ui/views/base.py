from PySide6.QtWidgets import QWidget, QDialog, QTableWidget, QMessageBox, QLabel
from PySide6.QtCore import Qt


class BaseObject:
    def __init__(self):
        pass

    def _set_label(self, label: QLabel, message: str, is_error: bool = False):
        label.setText(message)
        if is_error:
            label.setStyleSheet("color: red;")
        else:
            label.setStyleSheet("")


class BaseWidget(QWidget, BaseObject):
    def __init__(self):
        super().__init__()

    def get_selected_row_id(self, table: QTableWidget) -> int | None:
        selected_items = table.selectedItems()
        if not selected_items:
            return None

        # Check all items for a valid UserRole data
        for item in selected_items:
            item_id = item.data(Qt.ItemDataRole.UserRole)
            if item_id is not None:
                return item_id

        return selected_items[item_id].data(Qt.ItemDataRole.UserRole)

    def ask_for_confirmation(self, message: str) -> bool:
        reply = QMessageBox.question(
            self,
            "Confirm Action",
            message,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        return reply == QMessageBox.StandardButton.Yes


class BaseDialog(QDialog, BaseObject):
    def __init__(self, parent=None):
        super().__init__(parent)
