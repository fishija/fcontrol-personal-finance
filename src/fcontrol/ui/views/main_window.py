from PySide6.QtWidgets import QMainWindow, QButtonGroup

from fcontrol.ui.qt_generated.main_window import Ui_MainWindow
from fcontrol.ui.views import home_widget, allocation_widget, pockets_widget


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Setup
        self._setup_stacked_widget()
        self._setup_navigation_buttons()

    def _setup_stacked_widget(self):
        # Initialize and add widgets to the stacked widget
        self.home_widget = home_widget.HomeWidget()
        self.allocate_widget = allocation_widget.AllocationWidget()
        self.pockets_widget = pockets_widget.PocketsWidget()

        self.stackedWidget.addWidget(self.home_widget)
        self.stackedWidget.addWidget(self.allocate_widget)
        self.stackedWidget.addWidget(self.pockets_widget)

    def _setup_navigation_buttons(self):
        # Group buttons for navigation
        self.nav_button_group = QButtonGroup(self)

        self.nav_button_group.addButton(self.homeButton, 0)
        self.nav_button_group.addButton(self.allocateButton, 1)
        self.nav_button_group.addButton(self.pocketsButton, 2)

        # Set buttons to be checkable
        for button in self.nav_button_group.buttons():
            button.setCheckable(True)

        # Set buttons inside group to be exclusive
        self.nav_button_group.setExclusive(True)

        # Set default checked button
        self.homeButton.setChecked(True)

        # Connect button group signal to change stacked widget page
        self.nav_button_group.idClicked.connect(self._on_nav_button_clicked)

    def _on_nav_button_clicked(self, id):
        self.stackedWidget.setCurrentIndex(id)
