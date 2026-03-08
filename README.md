# Items API

## Overview
Items API is a FastAPI project with a layered architecture for clean separation of concerns.
It provides endpoints to create and fetch items stored in SQLite.

## Stack
- Python 3
- FastAPI
- Pydantic v2
- SQLite

## Project Structure
- `main.py`: app bootstrap, lifespan startup, router registration.
- `routes/items_routes.py`: HTTP routes and request/response mapping.
- `controllers/items_controller.py`: controller functions used by routes.
- `services/items_service.py`: business logic layer.
- `repositories/items_repository.py`: SQL access layer.
- `schemas/itemSchemas.py`: input/output schemas and validation.
- `responses/base_response.py`: standard API response envelope.
- `database/connection.py`: DB connection and schema initialization.

## Data Model
Table: `items`
- `id` INTEGER PRIMARY KEY AUTOINCREMENT
- `body` TEXT NOT NULL
- `created_at` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP

## API Endpoints
- `GET /` health check.
- `POST /items/` create a new item.
- `GET /items/?limit=100&offset=0` list items with pagination.
- `GET /items/latest/` get latest item.
- `GET /items/{item_id}/` get item by id.

### Create Payload
```json
{
  "body": "some text with at least 5 non-space characters"
}
```

## Response Format
All successful responses use the same envelope:

```json
{
  "success": true,
  "message": "Success",
  "data": {}
}
```

## Validation Rules
- `body` is trimmed before persistence.
- `body` min length: 5 non-space characters.
- `body` max length: 280 characters.
- `limit`: between 1 and 100.
- `offset`: 0 or greater.

## How to Create the Database

### Option 1: Automatic (recommended)
Start the app. The database and table are initialized at startup:

```bash
python3 main.py
```

### Option 2: Manual initialization script
Run only the DB initializer:

```bash
python3 -c "from database.connection import init_db; init_db()"
```

## How the Database Connection Works
Connection helper is implemented in `database/connection.py`.

- `get_connection()` opens a SQLite connection to `database/database.db`.
- Row factory is set to `sqlite3.Row` so query results can be converted to dicts.
- `init_db()` creates `items` table if needed and performs a backward-compatible `created_at` migration.

Example:

```python
from database.connection import get_connection

with get_connection() as connection:
    rows = connection.execute(
        "SELECT id, body, created_at FROM items ORDER BY id DESC LIMIT 10"
    ).fetchall()
    data = [dict(row) for row in rows]
    print(data)
```
