from fcontrol.ui import PocketsWidget, PocketEditDialog
from fcontrol.models import PocketRepository, Pocket


class PocketController:
    def __init__(self, view: PocketsWidget, repository: PocketRepository):
        self.view = view
        self.repository = repository

        self._connect_signals()
        self.refresh()

    def _connect_signals(self):
        self.view.add_request.connect(self._on_add)
        self.view.edit_request.connect(self._on_edit)
        self.view.delete_request.connect(self._on_delete)

    def _on_add(self, name: str, balance: float, currency: str):
        new_pocket = Pocket(name=name, balance=balance, currency=currency)
        new_pocket = self.repository.insert(new_pocket)
        print(f"insert pocket: {new_pocket}")

        self.refresh()

    def _on_edit(self, pocket_id: int):
        pocket = self.repository.get_by_id(pocket_id)
        if not pocket:
            print(f"Pocket with ID {pocket_id} not found.")
            return

        dialog = PocketEditDialog(pocket)
        if dialog.exec():
            new_values = dialog.get_values()
            pocket.name = new_values["name"]
            pocket.balance = new_values["balance"]
            pocket.currency = new_values["currency"]

            self.repository.update(pocket)
            self.refresh()

    def _on_delete(self, pocket_id: int):
        print(f"Delete pocket with ID: {pocket_id}")
        self.repository.delete(pocket_id)

        self.refresh()

    def refresh(self):
        pockets = self.repository.get_all()
        self.view.populate_table(pockets)
        print(f"Fetched pockets: {pockets}")
