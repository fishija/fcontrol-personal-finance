from dataclasses import dataclass, field
import datetime
from enum import Enum

from fcontrol.models import Pocket
from fcontrol.db_manager import DatabaseManager


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


class CategoryRepository:
    def __init__(self, db: DatabaseManager):
        self.db = db

    def get_all(self) -> list[Category]:
        rows = self.db.fetch_all("SELECT id, name, transaction_type FROM categories")
        return [
            Category(
                id=r["id"],
                name=r["name"],
                transaction_type=TransactionType(r["transaction_type"]),
            )
            for r in rows
        ]

    def get_by_id(self, category_id: int) -> Category | None:
        row = self.db.fetch_one(
            "SELECT id, name, transaction_type FROM categories WHERE id = ?",
            (category_id,),
        )
        if row:
            return Category(
                id=row["id"],
                name=row["name"],
                transaction_type=TransactionType(row["transaction_type"]),
            )
        return None

    def insert(self, category: Category) -> Category:
        category.id = self.db.execute(
            "INSERT INTO categories (name, transaction_type) VALUES (?, ?)",
            (category.name, category.transaction_type.value),
        )
        return category

    def update(self, category: Category) -> None:
        self.db.execute(
            "UPDATE categories SET name = ?, transaction_type = ? WHERE id = ?",
            (category.name, category.transaction_type.value, category.id),
        )

    def delete(self, category_id: int) -> None:
        self.db.execute("DELETE FROM categories WHERE id = ?", (category_id,))


class TransactionRepository:
    def __init__(self, db: DatabaseManager):
        self.db = db

    def get_all(self) -> list[Transaction]:
        rows = self.db.fetch_all(
            """
            SELECT t.id, t.amount, t.date, t.description,
                   p.id as pocket_id, p.name as pocket_name, p.balance as pocket_balance, p.currency as pocket_currency,
                   c.id as category_id, c.name as category_name, c.transaction_type as category_transaction_type
            FROM transactions t
            JOIN pockets p ON t.pocket_id = p.id
            JOIN categories c ON t.category_id = c.id
            ORDER BY t.date DESC
            """
        )
        return [
            Transaction(
                id=r["id"],
                amount=r["amount"],
                date=datetime.datetime.strptime(r["date"], "%Y-%m-%d").date(),
                description=r["description"],
                pocket=Pocket(
                    id=r["pocket_id"],
                    name=r["pocket_name"],
                    balance=r["pocket_balance"],
                    currency=r["pocket_currency"],
                ),
                category=Category(
                    id=r["category_id"],
                    name=r["category_name"],
                    transaction_type=TransactionType(r["category_transaction_type"]),
                ),
            )
            for r in rows
        ]

    def get_by_id(self, transaction_id: int) -> Transaction | None:
        row = self.db.fetch_one(
            """
            SELECT t.id, t.amount, t.date, t.description,
                   p.id as pocket_id, p.name as pocket_name, p.balance as pocket_balance, p.currency as pocket_currency,
                   c.id as category_id, c.name as category_name, c.transaction_type as category_transaction_type
            FROM transactions t
            JOIN pockets p ON t.pocket_id = p.id
            JOIN categories c ON t.category_id = c.id
            WHERE t.id = ?
            """,
            (transaction_id,),
        )
        if row:
            return Transaction(
                id=row["id"],
                amount=row["amount"],
                date=datetime.datetime.strptime(row["date"], "%Y-%m-%d").date(),
                description=row["description"],
                pocket=Pocket(
                    id=row["pocket_id"],
                    name=row["pocket_name"],
                    balance=row["pocket_balance"],
                    currency=row["pocket_currency"],
                ),
                category=Category(
                    id=row["category_id"],
                    name=row["category_name"],
                    transaction_type=TransactionType(row["category_transaction_type"]),
                ),
            )
        return None

    def insert(self, transaction: Transaction) -> Transaction:
        transaction.id = self.db.execute(
            """
            INSERT INTO transactions (amount, pocket_id, category_id, date, description)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                transaction.amount,
                transaction.pocket.id,
                transaction.category.id,
                transaction.date.isoformat(),
                transaction.description,
            ),
        )
        return transaction

    def update(self, transaction: Transaction) -> None:
        self.db.execute(
            """
            UPDATE transactions
            SET amount = ?, pocket_id = ?, category_id = ?, date = ?, description = ?
            WHERE id = ?
            """,
            (
                transaction.amount,
                transaction.pocket.id,
                transaction.category.id,
                transaction.date.isoformat(),
                transaction.description,
                transaction.id,
            ),
        )

    def delete(self, transaction_id: int) -> None:
        self.db.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
