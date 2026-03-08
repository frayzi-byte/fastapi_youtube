import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).resolve().parent / "database.db"


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_db() -> None:
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                body TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        columns = connection.execute("PRAGMA table_info(items)").fetchall()
        has_created_at = any(column["name"] == "created_at" for column in columns)
        if not has_created_at:
            connection.execute("ALTER TABLE items ADD COLUMN created_at TEXT")
            connection.execute(
                "UPDATE items SET created_at = CURRENT_TIMESTAMP WHERE created_at IS NULL"
            )
        connection.commit()
