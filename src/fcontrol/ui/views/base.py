import enum

from PySide6.QtWidgets import QWidget, QDialog, QMessageBox, QLabel
from PySide6.QtCore import Qt, QObject


class LabelState(enum.Enum):
    DEFAULT = "default"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"


class BaseObject:
    def __init__(self):
        pass

    def _set_label(
        self, label: QLabel, message: str, state: LabelState = LabelState.DEFAULT
    ):
        colors = {
            LabelState.SUCCESS: "color: green;",
            LabelState.WARNING: "color: orange;",
            LabelState.ERROR: "color: red;",
            LabelState.DEFAULT: "",
        }
        label.setText(message)
        label.setStyleSheet(colors[state])


class BaseWidget(QWidget, BaseObject):
    def __init__(self):
        super().__init__()

    def get_selected_row_id(self, obj: QObject) -> int | None:
        selected_items = obj.selectedItems()
        if not selected_items:
            return None

        # Check all items for a valid UserRole data
        for item in selected_items:
            item_id = item.data(Qt.ItemDataRole.UserRole)
            if item_id is not None:
                return item_id

        return None

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
