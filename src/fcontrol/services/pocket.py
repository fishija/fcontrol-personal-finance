from fcontrol.models import PocketRepository, Pocket


class PocketService:
    def __init__(self, repository: PocketRepository):
        self.repository = repository

    def validate_pocket_data(
        self, name: str, balance: float, currency: str
    ) -> str | None:
        if not name.strip():
            return "Pocket name cannot be empty."
        if balance < 0:
            return "Balance cannot be negative."
        if not currency.strip():
            return "Currency cannot be empty."
        return None

    def get_pockets(self) -> list[Pocket]:
        return self.repository.get_all()

    def get_pocket_by_id(self, pocket_id: int) -> Pocket | None:
        return self.repository.get_by_id(pocket_id)

    def add_pocket(self, name: str, balance: float, currency: str) -> str | None:
        error = self.validate_pocket_data(name, balance, currency)

        if error:
            return error

        new_pocket = Pocket(name=name, balance=balance, currency=currency)
        self.repository.insert(new_pocket)
        return None

    def delete_pocket(self, pocket_id: int) -> str | None:
        self.repository.delete(pocket_id)
        return None

    def update_pocket(
        self, pocket_id: int, name: str, balance: float, currency: str
    ) -> str | None:
        error = self.validate_pocket_data(name, balance, currency)

        if error:
            return error

        pocket = self.repository.get_by_id(pocket_id)
        if not pocket:
            return f"Pocket with ID {pocket_id} not found."

        pocket.name = name
        pocket.balance = balance
        pocket.currency = currency
        self.repository.update(pocket)
        return None
