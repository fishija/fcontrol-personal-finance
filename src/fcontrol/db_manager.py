import sqlite3


class DatabaseManager:
    def __init__(self, db_path: str):
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self._init_schema()
        self._migrate_schema()
        self._add_initial_data()

    def _init_schema(self):
        self.connection.executescript("""
            PRAGMA foreign_keys = ON;

            CREATE TABLE IF NOT EXISTS pockets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                balance REAL NOT NULL,
                currency TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS allocation_rules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pocket_id INTEGER,
                goal_id INTEGER,
                allocation_type TEXT NOT NULL,
                value REAL NOT NULL,
                position INTEGER NOT NULL,
                FOREIGN KEY (pocket_id) REFERENCES pockets(id) ON DELETE CASCADE,
                FOREIGN KEY (goal_id) REFERENCES goals(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            );

            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                pocket_id INTEGER NOT NULL,
                transaction_type TEXT NOT NULL,
                date TEXT NOT NULL,
                category_id INTEGER,
                source TEXT,
                description TEXT,
                FOREIGN KEY (pocket_id) REFERENCES pockets(id) ON DELETE CASCADE,
                FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
            );

            CREATE TABLE IF NOT EXISTS goals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                target_amount REAL NOT NULL,
                target_date TEXT,
                description TEXT,
                pocket_id INTEGER NOT NULL,
                FOREIGN KEY (pocket_id) REFERENCES pockets(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS goal_contributions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                goal_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL,
                note TEXT NOT NULL DEFAULT '',
                FOREIGN KEY (goal_id) REFERENCES goals(id) ON DELETE CASCADE
            );
        """)

    def _migrate_schema(self):
        pass

    def _add_initial_data(self):
        DEFAULT_CATEGORIES = [
            (1, "Salary"),
            (2, "Groceries"),
            (3, "Entertainment"),
            (4, "Utilities"),
            (5, "Transport"),
        ]

        self.connection.executemany(
            "INSERT OR IGNORE INTO categories (id, name) VALUES (?, ?)",
            DEFAULT_CATEGORIES,
        )
        self.connection.commit()

    def execute(self, query: str, params: tuple = ()) -> int:
        c = self.connection.execute(query, params)
        self.connection.commit()
        return c.lastrowid

    def fetch_all(self, query: str, params: tuple = ()) -> list[sqlite3.Row]:
        cursor = self.connection.execute(query, params)
        return cursor.fetchall()

    def fetch_one(self, query: str, params: tuple = ()) -> sqlite3.Row | None:
        cursor = self.connection.execute(query, params)
        return cursor.fetchone()

    def close(self):
        self.connection.close()
