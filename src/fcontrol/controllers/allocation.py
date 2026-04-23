from PySide6.QtCore import QObject

from fcontrol.ui import AllocationWidget, AllocationRuleEditDialog
from fcontrol.models import (
    PocketRepository,
    AllocationRule,
    AllocationType,
    AllocationRepository,
)
from fcontrol.services import AllocationService


class AllocationController(QObject):
    def __init__(
        self,
        view: AllocationWidget,
        pocket_repository: PocketRepository,
        allocation_repository: AllocationRepository,
        allocation_service: AllocationService,
    ):
        super().__init__()
        self.view = view
        self.pocket_repository = pocket_repository
        self.allocation_repository = allocation_repository
        self.allocation_service = allocation_service

        self._connect_signals()
        self.refresh()

    def _connect_signals(self):
        self.view.add_request.connect(self._on_add_allocation_rule)
        self.view.delete_request.connect(self._on_delete_allocation_rule)
        self.view.edit_request.connect(self._on_edit_allocation_rule)
        self.view.move_up_request.connect(self._on_move_up_allocation_rule)
        self.view.move_down_request.connect(self._on_move_down_allocation_rule)

        self.view.refresh_rules_request.connect(self.refresh_rules)
        self.view.calculate_request.connect(self._on_calculate_allocation)

    def _on_add_allocation_rule(
        self, pocket_id: int, allocation_type: str, value: float, position: int
    ):
        pocket = self.pocket_repository.get_by_id(pocket_id)
        if not pocket:
            print(f"Pocket with ID {pocket_id} not found.")
            return

        new_rule = AllocationRule(
            pocket=pocket,
            allocation_type=AllocationType(allocation_type),
            value=value,
            position=position,
        )
        self.allocation_repository.insert(new_rule)
        self.refresh_rules()

    def _on_delete_allocation_rule(self, rule_id: int):
        self.allocation_repository.delete(rule_id)
        self.refresh_rules()

    def _on_edit_allocation_rule(self, rule_id: int):
        rule = self.allocation_repository.get_by_id(rule_id)
        if not rule:
            print(f"Allocation rule with ID {rule_id} not found.")
            return

        pockets = self.pocket_repository.get_all()
        dialog = AllocationRuleEditDialog(rule, pockets, AllocationType)
        if dialog.exec_():
            new_values = dialog.get_values()

            pocket = self.pocket_repository.get_by_id(new_values["pocket_id"])
            if not pocket:
                print(f"Pocket with ID {new_values['pocket_id']} not found.")
                return

            rule.pocket = pocket
            rule.allocation_type = AllocationType(new_values["allocation_type"])
            rule.value = new_values["value"]
            self.allocation_repository.update(rule)
            self.refresh_rules()

    def _on_move_up_allocation_rule(self, rule_id: int):
        rule = self.allocation_repository.get_by_id(rule_id)
        if not rule:
            print(f"Allocation rule with ID {rule_id} not found.")
            return

        if rule.position > 0:
            previous_rule = self.allocation_repository.get_by_position(
                rule.position - 1
            )
            if previous_rule:
                previous_rule.position += 1
                rule.position -= 1
                self.allocation_repository.update(previous_rule)
                self.allocation_repository.update(rule)

        self.refresh_rules()

    def _on_move_down_allocation_rule(self, rule_id: int):
        rule = self.allocation_repository.get_by_id(rule_id)
        if not rule:
            print(f"Allocation rule with ID {rule_id} not found.")
            return

        if rule.position < self.allocation_repository.count() - 1:
            next_rule = self.allocation_repository.get_by_position(rule.position + 1)
            if next_rule:
                next_rule.position -= 1
                rule.position += 1
                self.allocation_repository.update(next_rule)
                self.allocation_repository.update(rule)

        self.refresh_rules()

    def _on_calculate_allocation(self, income_value: float, income_currency: str):
        pocket_balances = {
            pocket.id: pocket.balance for pocket in self.pocket_repository.get_all()
        }
        rules = self.allocation_repository.get_all()
        results = self.allocation_service.calculate(
            rules, pocket_balances, income_value, income_currency
        )
        self.view.display_calculation_results(results)

    def _reorder_rules(self, rules: list[AllocationRule]):
        for index, rule in enumerate(rules):
            rule.position = index
            self.allocation_repository.update(rule)

    def refresh_pockets(self):
        pockets = self.pocket_repository.get_all()
        self.view.populate_pockets(pockets)

    def refresh_rules(self):
        rules = self.allocation_repository.get_all()
        self.view.populate_rules(rules)

    def refresh(self):
        self.refresh_pockets()
        self.refresh_rules()
