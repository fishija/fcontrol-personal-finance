from PySide6.QtWidgets import QMainWindow, QButtonGroup

from fcontrol.ui.qt_generated.main_window import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, home_widget, allocation_widget, pockets_widget):
        super().__init__()
        self.setupUi(self)

        # Setup
        self._setup_stacked_widget(home_widget, allocation_widget, pockets_widget)
        self._setup_navigation_buttons()

    def _setup_stacked_widget(
        self,
        home_widget,
        allocation_widget,
        pockets_widget,
    ):
        # Initialize and add widgets to the stacked widget
        self.stackedWidget.addWidget(home_widget)
        self.stackedWidget.addWidget(allocation_widget)
        self.stackedWidget.addWidget(pockets_widget)

    def _setup_navigation_buttons(self):
        # Group buttons for navigation
        self.nav_button_group = QButtonGroup(self)

        self.nav_button_group.addButton(self.homeButton, 0)
        self.nav_button_group.addButton(self.allocationButton, 1)
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
        view = self.stackedWidget.currentWidget()
        if hasattr(view, "refresh"):
            view.refresh()
