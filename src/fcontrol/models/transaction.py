from dataclasses import dataclass, field
import datetime
from enum import Enum

from fcontrol.models import Pocket
from fcontrol.db_manager import DatabaseManager


class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


class TransactionSource(Enum):
    MANUAL = "manual"
    ALLOCATION = "allocation"
    ADJUSTMENT = "adjustment"
    OPENING_BALANCE = "opening_balance"


@dataclass
class TransactionCategory:
    name: str
    id: int | None = None


@dataclass
class Transaction:
    amount: float
    pocket: Pocket
    transaction_type: TransactionType
    date: datetime.date = field(default_factory=datetime.date.today)
    category: TransactionCategory = None
    source: TransactionSource = TransactionSource.MANUAL
    description: str = ""
    id: int | None = None

    @property
    def currency(self) -> str:
        return self.pocket.currency

    @property
    def signed_amount(self) -> float:
        return (
            self.amount
            if self.transaction_type == TransactionType.INCOME
            else -self.amount
        )

    @property
    def summary_short(self) -> str:
        return f"{self.amount} {self.currency} to {self.pocket.name}"

    @property
    def summary_long(self) -> str:
        return f"{self.date}: {self.amount} {self.currency} to {self.pocket.name} ({self.category.name})"


class TransactionCategoryRepository:
    def __init__(self, db: DatabaseManager):
        self.db = db

    def get_all(self) -> list[TransactionCategory]:
        rows = self.db.fetch_all("SELECT id, name FROM categories")
        return [TransactionCategory(id=r["id"], name=r["name"]) for r in rows]

    def get_by_id(self, category_id: int) -> TransactionCategory | None:
        row = self.db.fetch_one(
            "SELECT id, name FROM categories WHERE id = ?", (category_id,)
        )
        if row:
            return TransactionCategory(id=row["id"], name=row["name"])
        return None

    def insert(self, category: TransactionCategory) -> TransactionCategory:
        category.id = self.db.execute(
            "INSERT INTO categories (name) VALUES (?)", (category.name,)
        )
        return category

    def update(self, category: TransactionCategory) -> None:
        self.db.execute(
            "UPDATE categories SET name = ? WHERE id = ?", (category.name, category.id)
        )

    def delete(self, category_id: int) -> None:
        self.db.execute("DELETE FROM categories WHERE id = ?", (category_id,))


class TransactionRepository:
    def __init__(self, db: DatabaseManager):
        self.db = db

    def get_all(self) -> list[Transaction]:
        rows = self.db.fetch_all(
            """
            SELECT t.id, t.amount, t.date, t.description, t.transaction_type, t.source,
                   p.id as pocket_id, p.name as pocket_name, p.currency as pocket_currency,
                   c.id as category_id, c.name as category_name
            FROM transactions t
            JOIN pockets p ON t.pocket_id = p.id
            JOIN categories c ON t.category_id = c.id
            ORDER BY t.date DESC
            """
        )
        transactions = []
        for r in rows:
            pocket = Pocket(
                id=r["pocket_id"], name=r["pocket_name"], currency=r["pocket_currency"]
            )
            category = TransactionCategory(id=r["category_id"], name=r["category_name"])
            transaction = Transaction(
                id=r["id"],
                amount=r["amount"],
                date=datetime.datetime.strptime(r["date"], "%Y-%m-%d").date(),
                description=r["description"],
                transaction_type=TransactionType(r["transaction_type"]),
                source=TransactionSource(r["source"]),
                pocket=pocket,
                category=category,
            )
            transactions.append(transaction)
        return transactions

    def get_by_id(self, transaction_id: int) -> Transaction | None:
        row = self.db.fetch_one(
            """
            SELECT t.id, t.amount, t.date, t.description, t.transaction_type, t.source,
                   p.id as pocket_id, p.name as pocket_name, p.currency as pocket_currency,
                   c.id as category_id, c.name as category_name
            FROM transactions t
            JOIN pockets p ON t.pocket_id = p.id
            JOIN categories c ON t.category_id = c.id
            WHERE t.id = ?
            """,
            (transaction_id,),
        )
        if row:
            pocket = Pocket(
                id=row["pocket_id"],
                name=row["pocket_name"],
                currency=row["pocket_currency"],
            )
            category = TransactionCategory(
                id=row["category_id"], name=row["category_name"]
            )
            return Transaction(
                id=row["id"],
                amount=row["amount"],
                date=datetime.datetime.strptime(row["date"], "%Y-%m-%d").date(),
                description=row["description"],
                transaction_type=TransactionType(row["transaction_type"]),
                source=TransactionSource(row["source"]),
                pocket=pocket,
                category=category,
            )
        return None

    def insert(self, transaction: Transaction) -> Transaction:
        transaction.id = self.db.execute(
            """
            INSERT INTO transactions (amount, pocket_id, category_id, date, description, transaction_type, source)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                transaction.amount,
                transaction.pocket.id,
                transaction.category.id,
                transaction.date.isoformat(),
                transaction.description,
                transaction.transaction_type.value,
                transaction.source.value,
            ),
        )
        return transaction

    def update(self, transaction: Transaction) -> None:
        self.db.execute(
            """
            UPDATE transactions
            SET amount = ?, pocket_id = ?, category_id = ?, date = ?, description = ?, transaction_type = ?, source = ?
            WHERE id = ?
            """,
            (
                transaction.amount,
                transaction.pocket.id,
                transaction.category.id,
                transaction.date.isoformat(),
                transaction.description,
                transaction.transaction_type.value,
                transaction.source.value,
                transaction.id,
            ),
        )

    def delete(self, transaction_id: int) -> None:
        self.db.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
