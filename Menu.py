def Menu(texto, opciones):
    bandera = True
    valor = None
    while bandera:
        try:
            print(texto)
            valor = int(input("\nOpción: "))
            if 0 < valor <= opciones:
                bandera = False
            else:
                print("Opción no valida")
        except Exception as e:
            print("Opción no valida")
    return valor

if __name__ == "__main__":
    a = Menu("opciones del 1 al 5", 5)
    print(a)