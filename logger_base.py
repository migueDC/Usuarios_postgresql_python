import logging as log

log.basicConfig(level= log.DEBUG,
                format="%(levelname)s[%(filename)s: %(lineno)s]: %(asctime)s -> %(message)s",
                datefmt="%I:%M:%S %p",
                handlers=[
                    log.FileHandler("loboratorio_usuarios.log"),
                    log.StreamHandler()
                ])

if __name__ == "__main__":
    log.debug("Mensaje a nivel debug")