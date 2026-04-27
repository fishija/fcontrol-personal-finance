from PySide6.QtCore import QObject, Signal

from fcontrol.ui.views.base import LabelState
from fcontrol.ui import AllocationWidget, AllocationRuleEditDialog
from fcontrol.models import AllocationType, AllocationResult
from fcontrol.services import AllocationService


class AllocationController(QObject):
    apply_transactions_request = Signal(
        list, object
    )  # List of transactions to apply after allocation

    def __init__(
        self,
        view: AllocationWidget,
        allocation_service: AllocationService,
    ):
        super().__init__()
        self.view = view
        self.allocation_service = allocation_service

        self._connect_signals()
        self.refresh()

    def _connect_signals(self):
        self.view.add_request.connect(self._on_add_allocation_rule)
        self.view.delete_request.connect(self._on_delete_allocation_rule)
        self.view.edit_request.connect(self._on_edit_allocation_rule)
        self.view.move_up_request.connect(self._on_move_up_allocation_rule)
        self.view.move_down_request.connect(self._on_move_down_allocation_rule)
        self.view.income_changed.connect(self._on_income_changed)
        self.view.allocate_request.connect(self._on_allocate_clicked)

    def _on_add_allocation_rule(
        self, pocket_id: int, allocation_type: str, value: float, position: int
    ):
        try:
            error = self.allocation_service.add_rule(
                pocket_id, allocation_type, value, position
            )
            if error:
                self.view.set_info_message(error, LabelState.ERROR)
                return
        except Exception as e:
            self.view.set_info_message(
                f"Unexpected error when adding allocation rule: {str(e)}",
                LabelState.ERROR,
            )
            return

        self.refresh_rules()
        self.view.clear_new_rule_inputs()

    def _on_delete_allocation_rule(self, rule_id: int):
        try:
            self.allocation_service.delete_rule(rule_id)
        except Exception as e:
            self.view.set_info_message(
                f"Unexpected error when deleting rule: {str(e)}", LabelState.ERROR
            )
            return

        self.refresh_rules()

    def _on_edit_allocation_rule(self, rule_id: int):
        rule = self.allocation_service.get_rule_by_id(rule_id)
        if not rule:
            return

        pockets = self.allocation_service.get_pockets()
        dialog = AllocationRuleEditDialog(rule, pockets, AllocationType)
        if not dialog.exec_():
            return

        new_values = dialog.get_values()
        try:
            error = self.allocation_service.update_rule(
                rule_id,
                new_values["pocket_id"],
                new_values["allocation_type"],
                new_values["value"],
            )
            if error:
                self.view.set_info_message(error, LabelState.ERROR)
                return
        except Exception as e:
            self.view.set_info_message(f"Unexpected error: {e}", LabelState.ERROR)
            return

        self.refresh_rules()

    def _on_move_up_allocation_rule(self, rule_id: int):
        try:
            error = self.allocation_service.move_rule_up(rule_id)
            if error:
                # Do nothing
                return
            self.refresh_rules()
        except Exception as e:
            self.view.set_info_message(
                f"Unexpected error when moving rule: {str(e)}", LabelState.ERROR
            )

    def _on_move_down_allocation_rule(self, rule_id: int):
        try:
            error = self.allocation_service.move_rule_down(rule_id)
            if error:
                # Do nothing
                return
            self.refresh_rules()
        except Exception as e:
            self.view.set_info_message(
                f"Unexpected error when moving rule: {str(e)}", LabelState.ERROR
            )

    def _on_income_changed(self):
        self.refresh_rules()

    def _set_allocation_message(self, results: list[AllocationResult]):
        income_value, income_currency = self.view.get_income_data()
        validation_msg = self.allocation_service.validate_allocation_results(
            income_value, income_currency, results
        )

        if validation_msg:
            self.view.set_info_message(validation_msg, LabelState.WARNING)
        else:
            self.view.set_info_message("Allocation looks good!", LabelState.SUCCESS)

    def _on_allocate_clicked(self):
        # perform basic input validation before calling service method
        income_value, _ = self.view.get_income_data()
        transaction_category_id = self.view.get_selected_category_id()

        if income_value <= 0:
            self.view.set_info_message(
                "Please enter a valid income amount greater than 0.", LabelState.ERROR
            )
            return
        else:
            self.view.set_info_message("")

        # Input is valid, proceed with allocation
        try:
            # Create transactions based on allocation results and emit signal to apply them
            allocation_transactions = (
                self.allocation_service.create_allocation_transactions(
                    transaction_category_id
                )
            )
        except Exception as e:
            self.view.set_info_message(
                f"Unexpected error during allocation: {str(e)}", LabelState.ERROR
            )
            return

        # Emit signal with transactions to be applied by TransactionController
        self.apply_transactions_request.emit(
            allocation_transactions, self.on_allocation_performed
        )

    def on_allocation_performed(self, success: bool, message: str):
        if success:
            self.view.show_allocation_success_dialog(message)
            self.refresh_pockets()
            self.refresh_rules()
        else:
            self.view.set_info_message(message, LabelState.ERROR)

    def refresh_pockets(self):
        pockets = self.allocation_service.get_pockets()
        self.view.populate_pockets(pockets)

    def refresh_income_categories(self):
        categories = self.allocation_service.get_income_categories()
        self.view.populate_income_categories(categories)

    def refresh_rules(self):
        rules = self.allocation_service.get_allocation_rules()
        self.view.populate_rules(rules)

        # Get current income data to recalculate allocation results after refreshing rules
        income_input_value, income_currency = self.view.get_income_data()

        # Recalculate allocation after refreshing rules
        allocation_results = self.allocation_service.calculate_allocations(
            income_input_value, income_currency
        )

        # Update the view with new allocation results
        self.view.display_calculation_results(allocation_results)

        # Update allocation message based on new results
        self._set_allocation_message(allocation_results)

    def refresh(self):
        self.refresh_pockets()
        self.refresh_rules()
        self.refresh_income_categories()
