from fcontrol.models import (
    TransactionRepository,
    Transaction,
    TransactionCategory,
    TransactionCategoryRepository,
)


class TransactionService:
    def __init__(
        self,
        repository: TransactionRepository,
        transaction_category_repository: TransactionCategoryRepository,
    ):
        self.repository = repository
        self.transaction_category_repository = transaction_category_repository

    def get_transactions(self) -> list[Transaction]:
        return self.repository.get_all()
