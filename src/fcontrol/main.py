from PySide6.QtWidgets import QApplication
import sys

from fcontrol.ui import MainWindow
from fcontrol.config import APP_NAME, APP_VERSION


def main():
    # Initialize the Qt application
    app = QApplication(sys.argv)

    # Set application metadata
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)

    # Create and show the main window
    main_window = MainWindow()
    main_window.show()

    # Start the application event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
