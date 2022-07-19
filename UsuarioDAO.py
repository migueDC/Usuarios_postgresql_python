from logger_base import log
from Cursor_del_pool import Cursor_del_pool
from Usuario import Usuario

class UsuarioDAO:
    _SELECCIONAR = "SELECT * FROM usuario ORDER BY id_usuario"
    _INSERTAR = "INSERT INTO usuario (usuario, contraseña) VALUES(%s, %s)"
    _ACTUALIZAR = "UPDATE usuario SET usuario = %s, contraseña = %s WHERE id_usuario = %s"
    _ELIMINAR = "DELETE FROM usuario WHERE id_usuario = %s"

    @classmethod
    def seleccionar(cls):
        usuarios = []
        with Cursor_del_pool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            usuarioss = cursor.fetchall()
            for usuario in usuarioss:
                user = Usuario(usuario[1], usuario[2], usuario[0])
                usuarios.append(user)
        return usuarios

    @classmethod
    def insertar(cls, usuario):
        with Cursor_del_pool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Usuario a insertar: {usuario}")
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with Cursor_del_pool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Usuario a actializar: {usuario}")
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with Cursor_del_pool() as cursor:
            valores = (usuario.id,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Persona a eliminar: {usuario}")


if __name__ == "__main__":
    usuario1 = Usuario("fungi54","mamateamo",1)
    UsuarioDAO.eliminar(usuario1)


