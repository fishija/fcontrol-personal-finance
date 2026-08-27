from decimal import Decimal

from fcontrol.models import (
    PocketRepository,
    Pocket,
    Transaction,
    TransactionType,
    TransactionSource,
)


class PocketService:
    def __init__(
        self,
        pocket_repository: PocketRepository,
    ):
        self.pocket_repository = pocket_repository

    def validate_pocket_data(
        self, name: str, balance: Decimal, currency: str
    ) -> str | None:
        if not name.strip():
            return "Pocket name cannot be empty."
        if not currency.strip():
            return "Currency cannot be empty."
        return None

    def get_pockets(self) -> list[Pocket]:
        return self.pocket_repository.get_all()

    def get_pocket_by_id(self, pocket_id: int) -> Pocket | None:
        return self.pocket_repository.get_by_id(pocket_id)

    def create_add_transaction(
        self, name: str, balance: Decimal, currency: str
    ) -> Transaction:
        error = self.validate_pocket_data(name, balance, currency)
        if error:
            raise ValueError(error)

        new_pocket = Pocket(name=name, currency=currency)
        self.pocket_repository.insert(new_pocket)

        transaction_type = (
            TransactionType.INCOME if balance >= 0 else TransactionType.EXPENSE
        )

        # Create a transaction for the initial balance
        initial_transaction = Transaction(
            amount=abs(balance),
            transaction_type=transaction_type,
            source=TransactionSource.OPENING_BALANCE,
            pocket=new_pocket,
        )
        return initial_transaction

    def create_update_transaction(
        self, pocket: Pocket, name: str, balance: Decimal, currency: str
    ) -> Transaction:
        error = self.validate_pocket_data(name, balance, currency)
        if error:
            raise ValueError(error)

        # Update the pocket details
        pocket.name = name
        pocket.currency = currency
        self.pocket_repository.update(pocket)

        # Calculate the difference in balance
        balance_diff = balance - pocket.balance

        # Create a transaction for the balance change if there is a difference
        if balance_diff != 0:
            transaction_type = (
                TransactionType.INCOME if balance_diff > 0 else TransactionType.EXPENSE
            )
            update_transaction = Transaction(
                amount=abs(balance_diff),
                transaction_type=transaction_type,
                source=TransactionSource.ADJUSTMENT,
                pocket=pocket,
            )
            return update_transaction
        return None

    def delete_pocket(self, pocket_id: int):
        # simply delete the pocket, the transactions for that pocket will be deleted by cascade in the database
        pocket = self.pocket_repository.get_by_id(pocket_id)
        if not pocket:
            return None
        self.pocket_repository.delete(pocket_id)
