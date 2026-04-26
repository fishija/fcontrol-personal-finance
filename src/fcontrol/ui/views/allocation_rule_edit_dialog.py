from fcontrol.ui.views.base import BaseDialog, LabelState
from fcontrol.ui.qt_generated.allocation_rule_edit_dialog import (
    Ui_AllocationRuleEditDialog,
)


class AllocationRuleEditDialog(Ui_AllocationRuleEditDialog, BaseDialog):
    def __init__(self, allocation_rule, pockets, allocation_types, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.allocation_rule = allocation_rule
        self.pockets = pockets
        self.allocation_types = allocation_types

        self._setup_inputs()
        self._connect_signals()

        self.infoLabel.setText("")

    def _setup_inputs(self):
        for pocket in self.pockets:
            self.pocketSelect.addItem(f"{pocket.name} ({pocket.currency})", pocket.id)

        self.allocationTypeSelect.addItems(
            [atype.value for atype in self.allocation_types]
        )

        self.ruleValueInput.setMinimum(0)
        self.ruleValueInput.setMaximum(100_000_000)
        self.ruleValueInput.setDecimals(2)

        # Set current values
        if not self.allocation_rule:
            return

        pocket = self.allocation_rule.pocket
        self.pocketSelect.setCurrentText(f"{pocket.name} ({pocket.currency})")
        self.allocationTypeSelect.setCurrentText(
            self.allocation_rule.allocation_type.value
        )
        self.ruleValueInput.setValue(self.allocation_rule.value)

    def _connect_signals(self):
        self.saveButton.clicked.connect(self._on_save_clicked)
        self.cancelButton.clicked.connect(self.reject)

    def _on_save_clicked(self):
        if self.ruleValueInput.value() <= 0:
            self._set_label(
                self.infoLabel, "Value must be greater than 0.", LabelState.ERROR
            )
            return
        else:
            self._set_label(self.infoLabel, "")

        self.accept()

    def get_values(self):
        return {
            "pocket_id": self.pocketSelect.currentData(),
            "allocation_type": self.allocationTypeSelect.currentText(),
            "value": self.ruleValueInput.value(),
        }
