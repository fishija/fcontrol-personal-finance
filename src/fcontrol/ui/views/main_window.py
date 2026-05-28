from PySide6.QtWidgets import QMainWindow, QButtonGroup

from fcontrol.ui.qt_generated.main_window import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(
        self,
        home_widget,
        allocation_widget,
        pockets_widget,
        transactions_widget,
        goals_widget,
        net_worth_widget,
    ):
        super().__init__()
        self.setupUi(self)

        # Setup
        self._setup_nav_map(
            home_widget,
            allocation_widget,
            pockets_widget,
            transactions_widget,
            goals_widget,
            net_worth_widget,
        )
        self._setup_stacked_widget()
        self._setup_navigation_buttons()

    def _setup_nav_map(
        self,
        home_widget,
        allocation_widget,
        pockets_widget,
        transactions_widget,
        goals_widget,
        net_worth_widget,
    ):
        self.nav_map = {
            0: (self.homeButton, home_widget),
            1: (self.allocationButton, allocation_widget),
            2: (self.pocketsButton, pockets_widget),
            3: (self.transactionsButton, transactions_widget),
            4: (self.goalsButton, goals_widget),
            5: (self.netWorthButton, net_worth_widget),
        }

    def _setup_stacked_widget(self):
        # Initialize and add widgets to the stacked widget
        for _, widget in self.nav_map.values():
            self.stackedWidget.addWidget(widget)

    def _setup_navigation_buttons(self):
        # Group buttons for navigation
        self.nav_button_group = QButtonGroup(self)

        for nav_id, (button, _) in self.nav_map.items():
            self.nav_button_group.addButton(button, nav_id)

        # Set buttons to be checkable
        for button in self.nav_button_group.buttons():
            button.setCheckable(True)

        # Set buttons inside group to be exclusive
        self.nav_button_group.setExclusive(True)

        # Set default checked button
        self.homeButton.setChecked(True)

        # Connect button group signal to change stacked widget page
        self.nav_button_group.idClicked.connect(self._on_nav_button_clicked)

    def _on_nav_button_clicked(self, nav_id):
        self.stackedWidget.setCurrentIndex(nav_id)
        view = self.stackedWidget.currentWidget()
        if hasattr(view, "refresh"):
            view.refresh()
