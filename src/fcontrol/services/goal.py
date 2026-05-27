from fcontrol.models import (
    Goal,
    GoalRepository,
    GoalContribution,
    GoalContributionRepository,
    Pocket,
    PocketRepository,
)

import datetime


class GoalService:
    def __init__(
        self,
        goal_repository: GoalRepository,
        pocket_repository: PocketRepository,
        goal_contribution_repository: GoalContributionRepository,
    ):
        self.goal_repository = goal_repository
        self.pocket_repository = pocket_repository
        self.goal_contribution_repository = goal_contribution_repository

    def validate_goal_data(
        self,
        name: str,
        pocket_id: int,
        target_amount: float,
        target_date: datetime.date | None,
        description: str,
    ) -> str | None:
        if not name.strip():
            return "Goal name cannot be empty."
        if target_amount <= 0:
            return "Target amount must be greater than zero."
        if target_date and target_date < datetime.date.today():
            return "Target date cannot be in the past."
        return None

    def get_goals(self) -> list[Goal]:
        return self.goal_repository.get_all()

    def get_pockets(self) -> list[Pocket]:
        return self.pocket_repository.get_all()

    def get_goal_by_id(self, goal_id: int) -> Goal | None:
        return self.goal_repository.get_by_id(goal_id)

    def add_goal(
        self,
        name: str,
        pocket_id: int,
        target_amount: float,
        target_date: datetime.date | None,
        description: str,
    ) -> Goal:
        error = self.validate_goal_data(
            name, pocket_id, target_amount, target_date, description
        )
        if error:
            raise ValueError(error)

        pocket = self.pocket_repository.get_by_id(pocket_id)
        if pocket is None:
            raise ValueError("Selected pocket does not exist.")

        new_goal = Goal(
            name=name,
            pocket=pocket,
            target_amount=target_amount,
            target_date=target_date,
            description=description,
        )
        self.goal_repository.insert(new_goal)
        return new_goal

    def delete_goal(self, goal_id: int):
        self.goal_repository.delete(goal_id)

    def update_goal(
        self,
        goal: Goal,
        name: str,
        pocket_id: int,
        target_amount: float,
        target_date: datetime.date | None,
        description: str,
    ) -> Goal:
        error = self.validate_goal_data(
            name, pocket_id, target_amount, target_date, description
        )
        if error:
            raise ValueError(error)

        pocket = self.pocket_repository.get_by_id(pocket_id)
        if pocket is None:
            raise ValueError("Selected pocket does not exist.")

        goal.name = name
        goal.pocket = pocket
        goal.target_amount = target_amount
        goal.target_date = target_date
        goal.description = description

        self.goal_repository.update(goal)
        return goal

    def get_contributions(self, goal_id: int) -> list[GoalContribution]:
        return self.goal_contribution_repository.get_all_for_goal(goal_id)

    def add_contribution(
        self,
        goal_id: int,
        amount: float,
        date: datetime.date,
        note: str = "",
    ) -> GoalContribution:
        if amount <= 0:
            raise ValueError("Contribution amount must be greater than zero.")
        contribution = GoalContribution(
            goal_id=goal_id,
            amount=amount,
            date=date,
            note=note,
        )
        self.goal_contribution_repository.insert(contribution)
        return contribution

    def delete_contribution(self, contribution_id: int) -> None:
        self.goal_contribution_repository.delete(contribution_id)
