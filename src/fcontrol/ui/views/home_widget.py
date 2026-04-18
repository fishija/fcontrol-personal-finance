from PySide6.QtWidgets import QWidget

from fcontrol.ui.qt_generated.home_widget import Ui_HomeWidget


class HomeWidget(Ui_HomeWidget, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
