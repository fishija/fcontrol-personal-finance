from PySide6.QtWidgets import QWidget

from fcontrol.ui.views.base import BaseWidget
from fcontrol.ui.qt_generated.goals_widget import Ui_GoalsWidget


class GoalsWidget(Ui_GoalsWidget, BaseWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
