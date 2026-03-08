from database.connection import get_connection


class ItemsRepository:
    def add(self, item_dict: dict) -> dict:
        with get_connection() as connection:
            connection.execute(
                "INSERT INTO items (id, body) VALUES (?, ?)",
                (item_dict["id"], item_dict["body"]),
            )
            connection.commit()
        return item_dict

    def list_all(self) -> list:
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT id, body FROM items ORDER BY id ASC"
            ).fetchall()
        return [dict(row) for row in rows]

    def get_latest(self) -> dict | None:
        with get_connection() as connection:
            row = connection.execute(
                "SELECT id, body FROM items ORDER BY id DESC LIMIT 1"
            ).fetchone()
        return dict(row) if row else None

    def get_by_id(self, item_id: int) -> dict | None:
        with get_connection() as connection:
            row = connection.execute(
                "SELECT id, body FROM items WHERE id = ?",
                (item_id,),
            ).fetchone()
        return dict(row) if row else None
