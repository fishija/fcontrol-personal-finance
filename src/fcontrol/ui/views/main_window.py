from PySide6.QtWidgets import QApplication, QMainWindow

from fcontrol.ui.qt_generated.main_window import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Get application name and version from QApplication
        app = QApplication.instance()
        app_name = app.applicationName()
        app_version = app.applicationVersion()

        # Set window title with app name and version
        self.setWindowTitle(f"{app_name} {app_version}")

        # Setup
        self._setup_stacked_widget()
        self._setup_navigation_buttons()

    def _setup_stacked_widget(self):
        # Initialize and add widgets to the stacked widget
        pass

    def _setup_navigation_buttons(self):
        # Group buttons for navigation
        pass
