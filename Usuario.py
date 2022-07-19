from logger_base import  log

class Usuario:

    def __init__(self, username = None, password = None, id_user = None):
        self.__username = username
        self.__password = password
        self.__id = id_user

    def __str__(self):
        txt = "Usuario\n".center(50,"-")
        return txt + f"Id_persona: {self.__id}\tUsuario: {self.__username}\tPassword: {self.__password}"

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        self.__username = new_username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id


if __name__ == "__main__":
    persona1 = Usuario("fungi54", "315241475")
    log.debug(persona1)
    persona1.password = "mariposarosa"
    print(persona1.password)
    print(persona1[0])