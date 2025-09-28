import sqlite3
from typing import List
from models import Item

DB_PATH = "items.db"

class ItemDAO:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self._create_table_if_not_exists()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _create_table_if_not_exists(self):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                quantidade INTEGER NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def adicionar(self, item: Item) -> Item:
        """
        Adiciona Item ao banco e retorna o Item com id preenchido.
        """
        conn = self._connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO items (nome, descricao, quantidade) VALUES (?, ?, ?)",
            (item.nome, item.descricao, item.quantidade)
        )
        conn.commit()
        item_id = cur.lastrowid
        conn.close()
        return Item(id=item_id, nome=item.nome, descricao=item.descricao, quantidade=item.quantidade)

    def listarTodos(self) -> List[Item]:
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT id, nome, descricao, quantidade FROM items ORDER BY id")
        rows = cur.fetchall()
        conn.close()
        return [Item(id=row[0], nome=row[1], descricao=row[2], quantidade=row[3]) for row in rows]