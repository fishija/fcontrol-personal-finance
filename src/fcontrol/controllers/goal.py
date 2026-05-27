from PySide6.QtCore import QObject, Signal

from fcontrol.ui import GoalsWidget, GoalEditDialog
from fcontrol.services import GoalService


class GoalController(QObject):
    def __init__(self, view: GoalsWidget, service: GoalService):
        super().__init__()
        self.view = view
        self.service = service

        self._connect_signals()
        self.refresh()

    def _connect_signals(self):
        self.view.add_request.connect(self._on_add)
        self.view.edit_request.connect(self._on_edit)
        self.view.delete_request.connect(self._on_delete)

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
        except Exception as e:
            print(f"Unexpected error when deleting goal: {str(e)}")

    def refresh(self):
        goals = self.service.get_goals()
        pockets = self.service.get_pockets()

        self.view.populate_goal_list(goals)
        self.view.populate_pocket_select(pockets)
        self.view.refresh()
