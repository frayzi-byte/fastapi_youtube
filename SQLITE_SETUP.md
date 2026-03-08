# SQLite Setup and Connection Guide

This file explains how to create a SQLite database and how to connect to it in this project.

## 1. Where the database file lives

In this project, the DB path is defined in `database/connection.py`:

```python
DATABASE_PATH = Path(__file__).resolve().parent / "database.db"
```

So the final database file is:

`database/database.db`

## 2. Create the SQLite database

SQLite creates the database file automatically when the first connection is opened.

### Option A: Use the project initializer (recommended)

Run:

```bash
python3 -c "from database.connection import init_db; init_db()"
```

This will:
- create `database/database.db` if it does not exist
- create table `items` if it does not exist
- ensure `created_at` column exists (migration safety)

### Option B: Use sqlite3 CLI manually

Run:

```bash
sqlite3 database/database.db
```

Then execute:

```sql
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    body TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

Exit CLI with:

```sql
.quit
```

## 3. How to connect in Python

Use this pattern:

```python
import sqlite3
from pathlib import Path

db_path = Path("database/database.db")
connection = sqlite3.connect(db_path)
connection.row_factory = sqlite3.Row
connection.execute("PRAGMA foreign_keys = ON")
```

In this project, this logic is already centralized in `get_connection()` inside `database/connection.py`.

## 4. Read data example

```python
from database.connection import get_connection

with get_connection() as connection:
    rows = connection.execute(
        "SELECT id, body, created_at FROM items ORDER BY id DESC LIMIT 10"
    ).fetchall()
    data = [dict(row) for row in rows]
    print(data)
```

## 5. Write data example

```python
from database.connection import get_connection

with get_connection() as connection:
    connection.execute(
        "INSERT INTO items (body, created_at) VALUES (?, CURRENT_TIMESTAMP)",
        ("example item",),
    )
    connection.commit()
```

## 6. FastAPI startup behavior

`main.py` runs `init_db()` during app startup (lifespan), so starting the API is enough to initialize the database:

```bash
python3 main.py
```
