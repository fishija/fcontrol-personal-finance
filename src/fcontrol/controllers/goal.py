from PySide6.QtCore import QObject, Signal

from fcontrol.ui import GoalsWidget, GoalEditDialog, GoalContributionsDialog
from fcontrol.services import GoalService


class GoalController(QObject):
    goal_repo_changed = Signal()

    def __init__(self, view: GoalsWidget, service: GoalService):
        super().__init__()
        self.view = view
        self.service = service
        self._contributions_dialog = None
        self._contributions_goal_id = None

        self._connect_signals()
        self.refresh()

    def _connect_signals(self):
        self.view.add_request.connect(self._on_add)
        self.view.edit_request.connect(self._on_edit)
        self.view.delete_request.connect(self._on_delete)
        self.view.contributions_request.connect(self._on_contributions)

    def _on_add(
        self,
        name: str,
        pocket_id: int,
        target_amount: float,
        target_date,
        description: str,
    ):
        try:
            self.service.add_goal(
                name, pocket_id, target_amount, target_date, description
            )
            self.refresh()
            self.goal_repo_changed.emit()
        except Exception as e:
            print(f"Unexpected error when adding goal: {str(e)}")

    def _on_edit(self, goal_id: int):
        goal = self.service.get_goal_by_id(goal_id)
        if not goal:
            print(f"Goal with ID {goal_id} not found.")
            return

        pockets = self.service.get_pockets()
        dialog = GoalEditDialog(goal, pockets)
        if not dialog.exec():
            return

        new_values = dialog.get_values()
        try:
            self.service.update_goal(
                goal,
                new_values["name"],
                new_values["pocket_id"],
                new_values["target_amount"],
                new_values["target_date"],
                new_values["description"],
            )
            self.refresh()
        except Exception as e:
            print(f"Unexpected error when updating goal: {str(e)}")

    def _on_delete(self, goal_id: int):
        try:
            self.service.delete_goal(goal_id)
            self.refresh()
            self.goal_repo_changed.emit()
        except Exception as e:
            print(f"Unexpected error when deleting goal: {str(e)}")

    def _on_contributions(self, goal_id: int):
        goal = self.service.get_goal_by_id(goal_id)
        if not goal:
            print(f"Goal with ID {goal_id} not found.")
            return

        self._contributions_goal_id = goal_id
        contributions = self.service.get_contributions(goal_id)
        self._contributions_dialog = GoalContributionsDialog(goal, contributions)
        self._contributions_dialog.add_contribution_request.connect(
            self._on_add_contribution
        )
        self._contributions_dialog.delete_contribution_request.connect(
            self._on_delete_contribution
        )
        self._contributions_dialog.exec()
        self._contributions_goal_id = None
        self._contributions_dialog = None
        self.refresh()

    def _on_add_contribution(self, amount: float, date, note: str):
        goal_id = self._contributions_goal_id
        try:
            self.service.add_contribution(goal_id, amount, date, note)
            goal = self.service.get_goal_by_id(goal_id)
            contributions = self.service.get_contributions(goal_id)
            self._contributions_dialog.populate(goal, contributions)
            self.goal_repo_changed.emit()
        except Exception as e:
            print(f"Unexpected error when adding contribution: {str(e)}")

    def _on_delete_contribution(self, contribution_id: int):
        goal_id = self._contributions_goal_id
        try:
            self.service.delete_contribution(contribution_id)
            goal = self.service.get_goal_by_id(goal_id)
            contributions = self.service.get_contributions(goal_id)
            self._contributions_dialog.populate(goal, contributions)
            self.goal_repo_changed.emit()
        except Exception as e:
            print(f"Unexpected error when removing contribution: {str(e)}")

    def refresh(self):
        goals = self.service.get_goals()
        pockets = self.service.get_pockets()

        self.view.populate_goal_list(goals)
        self.view.populate_pocket_select(pockets)
        self.view.refresh()
