from logger_base import log
from Conexion import  Conexion

class Cursor_del_pool:
    def __init__(self):
        self.__conexion = None
        self.__cursor = None

    def __enter__(self):
        self.__conexion = Conexion.obtener_conexion()
        self.__cursor = self.__conexion.cursor()
        return self.__cursor

    def __exit__(self, exeption_type, exeption_value, exeption_detail):
        if exeption_type:
            log.error(f"Ocurrio en error, se hace rollback: {exeption_type} {exeption_value} {exeption_detail}")
            self.__conexion.rollback()
        else:
            log.debug("Se hace commmit de la transaccion")
            self.__conexion.commit()
        self.__cursor.close()
        Conexion.liberar_conexion(self.__conexion)

if __name__ == "__main__":
    with Cursor_del_pool() as cursor:
        cursor.execute("SELECT * FROM usuario")
        log.debug(cursor.fetchall())