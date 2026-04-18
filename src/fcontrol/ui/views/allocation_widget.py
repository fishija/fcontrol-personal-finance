from PySide6.QtWidgets import QWidget

from fcontrol.ui.qt_generated.allocation_widget import Ui_AllocationWidget


class AllocationWidget(Ui_AllocationWidget, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
