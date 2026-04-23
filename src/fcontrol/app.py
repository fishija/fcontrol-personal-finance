import atexit
from PySide6.QtWidgets import QApplication
from currency_converter import CurrencyConverter
from fcontrol.config import APP_NAME, APP_VERSION, DB_PATH
from fcontrol.db_manager import DatabaseManager
from fcontrol.models import PocketRepository, AllocationRepository
from fcontrol.services import AllocationService
from fcontrol.controllers import PocketController, AllocationController
from fcontrol.ui import MainWindow, HomeWidget, AllocationWidget, PocketsWidget


class Application:
    def __init__(self, argv):
        self.qt_app = QApplication(argv)
        self.qt_app.setOrganizationName("jm")
        self.qt_app.setApplicationName(APP_NAME)
        self.qt_app.setApplicationVersion(APP_VERSION)

        self._setup_currency_converter()
        self._setup_database()
        self._setup_repositories()
        self._setup_views()
        self._setup_services()
        self._setup_controllers()
        self._setup_main_window()

    def _setup_currency_converter(self):
        self.currency_converter = CurrencyConverter()

    def _setup_database(self):
        self.db = DatabaseManager(DB_PATH)
        atexit.register(self.db.close)

    def _setup_repositories(self):
        self.pocket_repository = PocketRepository(self.db)
        self.allocation_repository = AllocationRepository(
            self.db, self.pocket_repository
        )

    def _setup_views(self):
        self.home_widget = HomeWidget()
        self.allocation_widget = AllocationWidget()
        self.pockets_widget = PocketsWidget()

    def _setup_services(self):
        self.allocation_service = AllocationService(self.currency_converter)

    def _setup_controllers(self):
        self.pocket_controller = PocketController(
            self.pockets_widget, self.pocket_repository
        )
        self.allocation_controller = AllocationController(
            self.allocation_widget,
            self.pocket_repository,
            self.allocation_repository,
            self.allocation_service,
        )

        # Connections between controllers
        self.pocket_controller.pocket_repo_changed.connect(
            self.allocation_controller.refresh
        )

    def _setup_main_window(self):
        self.main_window = MainWindow(
            home_widget=self.home_widget,
            allocation_widget=self.allocation_widget,
            pockets_widget=self.pockets_widget,
        )
        self.main_window.setWindowTitle(f"{APP_NAME} {APP_VERSION}")

    def run(self) -> int:
        self.main_window.show()
        return self.qt_app.exec()
