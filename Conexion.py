import sys

from logger_base import log
from psycopg2 import pool
class Conexion:
    _DATABASE = "test_db"
    _USERNAME = "postgres"
    _HOST = "127.0.0.1"
    _PORT = 5432
    _PASSWORD = "admin"
    _MIN_CONN = 1
    _MAX_CONN = 5
    _POOL = None

    @classmethod
    def obtener_pool(cls):
        if cls._POOL == None:
            try:
                cls._POOL = pool.SimpleConnectionPool(cls._MIN_CONN, cls._MAX_CONN, host = cls._HOST,
                                                      user = cls._USERNAME, password = cls._PASSWORD,
                                                      port = cls._PORT, database = cls._DATABASE)
                log.debug(f"Creacion exitosa del pool: {cls._POOL}")
            except Exception as e:
                log.error(f"Ocurrio un error al abrir el pool: {e}")
                sys.exit()
        else:
            pass
        return cls._POOL

    @classmethod
    def obtener_conexion(cls):
        conexion = Conexion.obtener_pool().getconn()
        log.debug(f"Se obtuvo conexion: {conexion}")
        return  conexion

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion = Conexion.obtener_pool().putconn(conexion)
        log.debug(f"Se libero la conexion: {conexion}")

    @classmethod
    def cerrar_conexiones(cls):
        Conexion.obtener_pool().closeall()
        log.debug(f"Se serro el pool")

if __name__ == "__main__":
    conexion1 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion1)
    conexion2 = Conexion.obtener_conexion()
    Conexion.cerrar_conexiones()