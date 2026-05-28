from PySide6.QtWidgets import QComboBox, QSizePolicy
from fcontrol.ui.views.base import BaseDialog, LabelState
from fcontrol.ui.qt_generated.allocation_rule_edit_dialog import (
    Ui_AllocationRuleEditDialog,
)


class AllocationRuleEditDialog(Ui_AllocationRuleEditDialog, BaseDialog):
    def __init__(
        self, allocation_rule, pockets, allocation_types, goals=None, parent=None
    ):
        super().__init__(parent)
        self.setupUi(self)

        self.allocation_rule = allocation_rule
        self.pockets = pockets
        self.allocation_types = allocation_types
        self.goals = goals or []

        self._setup_goal_select()
        self._setup_inputs()
        self._connect_signals()

        self.infoLabel.setText("")

    def _setup_goal_select(self):
        """Add a goal select inline with the pocket select, separated by /."""
        self.goalSelect = QComboBox(self.groupBox)
        self.goalSelect.setObjectName("goalSelect")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHeightForWidth(self.goalSelect.sizePolicy().hasHeightForWidth())
        self.goalSelect.setSizePolicy(sizePolicy)

        # Change the trailing label to "/" separator
        self.label_4.setText("/")

        # Insert goal select after the "/" label in the pocket row
        self.horizontalLayout_2.insertWidget(
            self.horizontalLayout_2.indexOf(self.label_4) + 1, self.goalSelect
        )

    def _setup_inputs(self):
        self.pocketSelect.addItem("Select Pocket", None)
        for pocket in self.pockets:
            self.pocketSelect.addItem(f"{pocket.name} ({pocket.currency})", pocket.id)

        self.goalSelect.addItem("Select Goal", None)
        for goal in self.goals:
            self.goalSelect.addItem(f"{goal.name} ({goal.pocket.currency})", goal.id)

        self.allocationTypeSelect.addItems(
            [atype.value for atype in self.allocation_types]
        )

        self.ruleValueInput.setMinimum(0)
        self.ruleValueInput.setMaximum(100_000_000)
        self.ruleValueInput.setDecimals(2)

        # Set current values
        if not self.allocation_rule:
            return

        if self.allocation_rule.pocket:
            pocket = self.allocation_rule.pocket
            self.pocketSelect.setCurrentText(f"{pocket.name} ({pocket.currency})")
            self.goalSelect.setEnabled(False)
        else:
            self.pocketSelect.setCurrentIndex(0)

        if self.allocation_rule.goal:
            goal = self.allocation_rule.goal
            self.goalSelect.setCurrentText(f"{goal.name} ({goal.pocket.currency})")
            self.pocketSelect.setEnabled(False)
        else:
            self.goalSelect.setCurrentIndex(0)

        self.allocationTypeSelect.setCurrentText(
            self.allocation_rule.allocation_type.value
        )
        self.ruleValueInput.setValue(self.allocation_rule.value)

    def _connect_signals(self):
        self.saveButton.clicked.connect(self._on_save_clicked)
        self.cancelButton.clicked.connect(self.reject)
        self.pocketSelect.currentIndexChanged.connect(self._on_pocket_changed)
        self.goalSelect.currentIndexChanged.connect(self._on_goal_changed)

    def _on_pocket_changed(self):
        """When a pocket is selected, disable goal selection."""
        if self.pocketSelect.currentData() is not None:
            self.goalSelect.setEnabled(False)
        else:
            self.goalSelect.setEnabled(True)

    def _on_goal_changed(self):
        """When a goal is selected, disable pocket selection."""
        if self.goalSelect.currentData() is not None:
            self.pocketSelect.setEnabled(False)
        else:
            self.pocketSelect.setEnabled(True)

    def _on_save_clicked(self):
        if self.ruleValueInput.value() <= 0:
            self._set_label(
                self.infoLabel, "Value must be greater than 0.", LabelState.ERROR
            )
            return

        if (
            self.pocketSelect.currentData() is None
            and self.goalSelect.currentData() is None
        ):
            self._set_label(
                self.infoLabel, "Select a pocket or a goal.", LabelState.ERROR
            )
            return

        self._set_label(self.infoLabel, "")
        self.accept()

    def get_values(self):
        return {
            "pocket_id": self.pocketSelect.currentData(),
            "goal_id": self.goalSelect.currentData(),
            "allocation_type": self.allocationTypeSelect.currentText(),
            "value": self.ruleValueInput.value(),
        }
