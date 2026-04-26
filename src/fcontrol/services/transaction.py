from fcontrol.models import (
    TransactionRepository,
    Transaction,
    PocketRepository,
)


class TransactionService:
    def __init__(
        self,
        transaction_repository: TransactionRepository,
        pocket_repository: PocketRepository,
    ):
        self.transaction_repository = transaction_repository
        self.pocket_repository = pocket_repository

    def get_transactions(self) -> list[Transaction]:
        return self.transaction_repository.get_all()

    def apply_transaction(self, transaction: Transaction) -> None:
        # Update the pocket balance
        pocket = self.pocket_repository.get_by_id(transaction.pocket.id)
        if not pocket:
            raise ValueError(f"Pocket with ID {transaction.pocket.id} not found")

        pocket.balance += transaction.signed_amount
        self.pocket_repository.update(pocket)

        # Save the transaction
        self.transaction_repository.insert(transaction)
