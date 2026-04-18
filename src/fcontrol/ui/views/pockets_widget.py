from PySide6.QtWidgets import QWidget

from fcontrol.ui.qt_generated.pockets_widget import Ui_PocketsWidget


class PocketsWidget(Ui_PocketsWidget, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
