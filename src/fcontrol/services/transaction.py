from fcontrol.models import (
    Transaction,
    TransactionCategory,
    PocketRepository,
    TransactionRepository,
    TransactionCategoryRepository,
)


class TransactionService:
    def __init__(
        self,
        transaction_repository: TransactionRepository,
        transaction_category_repository: TransactionCategoryRepository,
        pocket_repository: PocketRepository,
    ):
        self.transaction_repository = transaction_repository
        self.transaction_category_repository = transaction_category_repository
        self.pocket_repository = pocket_repository

    def get_transactions(self) -> list[Transaction]:
        return self.transaction_repository.get_all()

    def get_categories(self) -> list[str]:
        return self.transaction_category_repository.get_all()

    def add_category(self, category_name: str) -> None:
        category = TransactionCategory(name=category_name)
        self.transaction_category_repository.insert(category)

    def delete_category(self, category_id: int) -> None:
        category = self.transaction_category_repository.get_by_id(category_id)
        if not category:
            raise ValueError(f"Category with ID '{category_id}' not found")
        self.transaction_category_repository.delete(category.id)

    def apply_transaction(self, transaction: Transaction) -> None:
        # Update the pocket balance
        pocket = self.pocket_repository.get_by_id(transaction.pocket.id)
        if not pocket:
            raise ValueError(f"Pocket with ID {transaction.pocket.id} not found")

        pocket.balance += transaction.signed_amount
        self.pocket_repository.update(pocket)

        # Save the transaction only if it has a non-zero amount
        if transaction.signed_amount != 0:
            self.transaction_repository.insert(transaction)
