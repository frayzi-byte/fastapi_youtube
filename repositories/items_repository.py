from database.connection import get_connection


class ItemsRepository:
    def add(self, body: str) -> dict:
        with get_connection() as connection:
            cursor = connection.execute(
                "INSERT INTO items (body, created_at) VALUES (?, CURRENT_TIMESTAMP)",
                (body,),
            )
            connection.commit()
            row = connection.execute(
                "SELECT id, body, created_at FROM items WHERE id = ?",
                (cursor.lastrowid,),
            ).fetchone()
        if not row:
            raise RuntimeError("failed to fetch inserted item")
        return dict(row)

    def list_all(self, limit: int = 100, offset: int = 0) -> list[dict]:
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT id, body, created_at
                FROM items
                ORDER BY id ASC
                LIMIT ? OFFSET ?
                """,
                (limit, offset),
            ).fetchall()
        return [dict(row) for row in rows]

    def get_latest(self) -> dict | None:
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT id, body, created_at
                FROM items
                ORDER BY datetime(created_at) DESC, id DESC
                LIMIT 1
                """
            ).fetchone()
        return dict(row) if row else None

    def get_by_id(self, item_id: int) -> dict | None:
        with get_connection() as connection:
            row = connection.execute(
                "SELECT id, body, created_at FROM items WHERE id = ?",
                (item_id,),
            ).fetchone()
        return dict(row) if row else None
