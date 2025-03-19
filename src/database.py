import sqlite3
import config

class DB_Manager(object):
    _conn: sqlite3.Connection

    def __init__(self) -> None:
        pass

    def open_connection(self) -> bool:
        try:
            conn = sqlite3.connect(config.DATABASE_PATH)
            self._conn = conn
        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            self._conn = None        

    def get_connection(self) -> sqlite3.Connection:
        if self._conn:
            return self._conn

    def close_connection(self):
        if self._conn:
            self._conn.close()
