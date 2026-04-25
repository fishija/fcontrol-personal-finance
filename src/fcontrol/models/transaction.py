from dataclasses import dataclass, field
import datetime
from enum import Enum

from fcontrol.models import Pocket


class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"
    # TRANSFER = "transfer"  # (between pockets) planned - requires cross-currency handling

    # ideas for future transactionTypes, not implemented yet
    # GOAL_CONTRIBUTION = "goal_contribution"
    # GOAL_WITHDRAWAL = "goal_withdrawal"  # when money is taken out of a goal
    # INVESTMENT_PROFIT = "investment_profit"
    # INVESTMENT_LOSS = "investment_loss"


@dataclass
class Category:
    name: str
    transaction_type: TransactionType
    id: int | None = None


@dataclass
class Transaction:
    amount: float
    pocket: Pocket
    category: Category
    date: datetime.date = field(default_factory=datetime.date.today)
    description: str = ""
    id: int | None = None

    @property
    def currency(self) -> str:
        return self.pocket.currency

    @property
    def transaction_type(self) -> TransactionType:
        return self.category.transaction_type
