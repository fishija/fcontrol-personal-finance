from fcontrol.models import (
    Transaction,
    TransactionCategory,
    PocketRepository,
    TransactionRepository,
    TransactionCategoryRepository,
    TransactionType,
    TransactionSource,
)

import datetime


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

    def get_pockets(self) -> list[str]:
        return self.pocket_repository.get_all()

    def add_category(self, category_name: str) -> None:
        category = TransactionCategory(name=category_name)
        self.transaction_category_repository.insert(category)

    def delete_category(self, category_id: int) -> None:
        category = self.transaction_category_repository.get_by_id(category_id)
        if not category:
            raise ValueError(f"Category with ID '{category_id}' not found")
        self.transaction_category_repository.delete(category.id)

    def add_transaction(
        self,
        amount: float,
        pocket_id: int,
        transaction_type: TransactionType,
        source: TransactionSource,
        date: datetime.date = datetime.date.today(),
        category_id: int | None = None,
        description: str = "",
    ) -> None:
        # Set pocket
        pocket = self.pocket_repository.get_by_id(pocket_id)
        if not pocket:
            raise ValueError(f"Pocket with ID '{pocket_id}' not found")

        # Set category if provided
        category = None
        if category_id is not None:
            category = self.transaction_category_repository.get_by_id(category_id)
            if not category:
                raise ValueError(f"Category with ID '{category_id}' not found")

        # Create the transaction
        transaction = Transaction(
            amount=amount,
            pocket=pocket,
            transaction_type=transaction_type,
            date=date,
            category=category,
            source=source,
            description=description,
        )
        self.apply_transaction(transaction)

    def delete_transaction(self, transaction_id: int) -> None:
        transaction = self.transaction_repository.get_by_id(transaction_id)
        if not transaction:
            raise ValueError(f"Transaction with ID '{transaction_id}' not found")

        # Get pocket associated with the transaction
        pocket = self.pocket_repository.get_by_id(transaction.pocket.id)
        if not pocket:
            raise ValueError(
                f"Associated pocket for transaction ID '{transaction_id}' not found"
            )

        # Reverse the transaction's effect on the pocket balance
        pocket.balance -= transaction.signed_amount

        # Now delete the transaction
        self.transaction_repository.delete(transaction.id)

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
