from logger_base import log
from Usuario import Usuario
from UsuarioDAO import UsuarioDAO
from Menu import Menu

bandera = True
texto = ("""
Base de datos Usuario:
Opciones:
1) Ver registros
2) Insertar
3) Actulizar
4) Eliminar
5) Salir""")
while bandera:
    opcion = Menu(texto, 5)
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.debug(usuario)

    elif opcion == 2:
        usuario = input("Nombre del usuario a insertar: ")
        contraseña = input("Contraseña del usuario: ")
        user = Usuario(usuario, contraseña)
        UsuarioDAO.insertar(user)

    elif opcion == 3:
        id = Menu("Id persona a actualizar", 100000)
        usuario = input("Nombre del usuario a actulizar: ")
        contraseña = input("Contraseña del usuario actulizada: ")
        user = Usuario(usuario, contraseña, id)
        UsuarioDAO.actualizar(user)

    elif opcion == 4:
        id = Menu("Id persona a eliminar", 100000)
        user = Usuario("","", id)
        UsuarioDAO.eliminar(user)

    else:
        bandera = False