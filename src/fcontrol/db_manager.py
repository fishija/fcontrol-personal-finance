import sqlite3


class DatabaseManager:
    def __init__(self, db_path: str):
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self):
        self.connection.executescript(
            """
            PRAGMA foreign_keys = ON;

            CREATE TABLE IF NOT EXISTS pockets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                balance REAL NOT NULL,
                currency TEXT NOT NULL
            );
        """
        )

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
