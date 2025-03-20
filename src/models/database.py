import sqlite3
import config

class DB_Manager(object):
    _conn: sqlite3.Connection
    
    @classmethod
    def open_connection(cls) -> bool:
        try:
            conn = sqlite3.connect(config.DATABASE_PATH)
            cls._conn = conn
        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            cls._conn = None        

    @classmethod
    def get_connection(cls) -> sqlite3.Connection:
        if not cls._conn:
            DB_Manager.open_connection()
        return cls._conn

    @classmethod
    def close_connection(cls):
        if cls._conn:
            cls._conn.close()
