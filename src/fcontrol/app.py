import atexit
from PySide6.QtWidgets import QApplication
from currency_converter import CurrencyConverter
from fcontrol.config import APP_NAME, APP_VERSION, DB_PATH
from fcontrol.db_manager import DatabaseManager
from fcontrol.models import (
    PocketRepository,
    AllocationRepository,
    TransactionRepository,
    TransactionCategoryRepository,
    GoalRepository,
    GoalContributionRepository,
)
from fcontrol.services import (
    PocketService,
    AllocationService,
    TransactionService,
    GoalService,
)
from fcontrol.controllers import (
    PocketController,
    AllocationController,
    TransactionController,
    GoalController,
)
from fcontrol.ui import (
    MainWindow,
    HomeWidget,
    AllocationWidget,
    PocketsWidget,
    TransactionsWidget,
    GoalsWidget,
)


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
        self._setup_controller_connections()
        self._setup_main_window()

    def _setup_currency_converter(self):
        self.currency_converter = CurrencyConverter()

    def _setup_database(self):
        self.db = DatabaseManager(DB_PATH)
        atexit.register(self.db.close)

    def _setup_repositories(self):
        self.pocket_repository = PocketRepository(self.db)
        self.goal_repository = GoalRepository(self.db)
        self.allocation_repository = AllocationRepository(
            self.db, self.pocket_repository, self.goal_repository
        )
        self.transaction_repository = TransactionRepository(self.db)
        self.transaction_category_repository = TransactionCategoryRepository(self.db)
        self.goal_contribution_repository = GoalContributionRepository(self.db)

    def _setup_views(self):
        self.home_widget = HomeWidget()
        self.allocation_widget = AllocationWidget()
        self.pockets_widget = PocketsWidget()
        self.transactions_widget = TransactionsWidget()
        self.goals_widget = GoalsWidget()

    def _setup_services(self):
        self.pocket_service = PocketService(self.pocket_repository)
        self.allocation_service = AllocationService(
            self.allocation_repository,
            self.pocket_repository,
            self.transaction_category_repository,
            self.currency_converter,
            self.goal_repository,
            self.goal_contribution_repository,
        )
        self.transaction_service = TransactionService(
            self.transaction_repository,
            self.transaction_category_repository,
            self.pocket_repository,
        )
        self.goal_service = GoalService(
            self.goal_repository,
            self.pocket_repository,
            self.goal_contribution_repository,
        )

    def _setup_controllers(self):
        self.pocket_controller = PocketController(
            self.pockets_widget, self.pocket_service
        )
        self.allocation_controller = AllocationController(
            self.allocation_widget, self.allocation_service
        )
        self.transaction_controller = TransactionController(
            self.transactions_widget, self.transaction_service
        )
        self.goal_controller = GoalController(self.goals_widget, self.goal_service)

    def _setup_controller_connections(self):
        # Connections between controllers - pocket
        self.pocket_controller.pocket_repo_changed.connect(
            self.allocation_controller.refresh
        )
        self.pocket_controller.pocket_repo_changed.connect(
            self.transaction_controller.refresh
        )
        self.pocket_controller.pocket_repo_changed.connect(self.goal_controller.refresh)

        # Connect apply transactions
        self.pocket_controller.apply_transactions_requested.connect(
            self.transaction_controller.apply_transactions
        )
        self.allocation_controller.apply_transactions_request.connect(
            self.transaction_controller.apply_transactions
        )

        # Connect allocation goal_repo_changed to refresh goal view
        self.allocation_controller.goal_repo_changed.connect(
            self.goal_controller.refresh
        )

        # Connect category repo changed
        self.transaction_controller.category_repo_changed.connect(
            self.allocation_controller.refresh
        )

        # Connections between controllers - goals
        self.goal_controller.goal_repo_changed.connect(self.pocket_controller.refresh)
        self.goal_controller.goal_repo_changed.connect(
            self.allocation_controller.refresh
        )

        # Connections between controllers - transactions
        self.transaction_controller.transaction_repo_changed.connect(
            self.pocket_controller.refresh
        )
        self.transaction_controller.transaction_repo_changed.connect(
            self.allocation_controller.refresh
        )
        self.transaction_controller.transaction_repo_changed.connect(
            self.goal_controller.refresh
        )

    def _setup_main_window(self):
        self.main_window = MainWindow(
            home_widget=self.home_widget,
            allocation_widget=self.allocation_widget,
            pockets_widget=self.pockets_widget,
            transactions_widget=self.transactions_widget,
            goals_widget=self.goals_widget,
        )
        self.main_window.setWindowTitle(f"{APP_NAME} {APP_VERSION}")

    def run(self) -> int:
        self.main_window.show()
        return self.qt_app.exec()
