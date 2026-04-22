from PySide6.QtWidgets import QDialog

from fcontrol.ui.qt_generated.allocation_rule_edit_dialog import (
    Ui_AllocationRuleEditDialog,
)
from fcontrol.config import CURRENCIES


class AllocationRuleEditDialog(Ui_AllocationRuleEditDialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
