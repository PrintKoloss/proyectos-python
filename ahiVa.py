dato = False
contador = 0

usuario = input("Ingresar usuario: ")

base_usuarios = ["pepe", "juan", "texto"]

if usuario in base_usuarios:
    dato = True
    contador += 1  # También se puede usar contador += 1

if dato:
    print("Calculo FC para Jersey y Frisa Invisible")
    print("____________________________________________")
    print(
        """Opciones:

        1. Jersey
        2. Frisa Invisible"""
    )

    # Asegúrate de que la elección sea un número válido
    try:
        eleccion = int(input("Ingresar el articulo que desea calcular FC: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        exit()  # Termina el programa si la entrada no es válida

    if eleccion == 1:
        print("--------------------------------------------------")
        print("            Factor de Cobertura Jersey            ")
        print("__________________________________________________")

        # Asegúrate de que el usuario ingrese valores numéricos
        try:
            titulo = float(input("Ingrese titulo de hilado: "))
            longitud_malla = float(input("Ingrese Longitud de Malla: "))
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")
            exit()  # Termina el programa si la entrada no es válida

        factor_jersey = conversion(titulo, longitud_malla)
        print(f"Factor de cobertura Jersey: {factor_jersey}")

    elif eleccion == 2:
        print("--------------------------------------------------")
        print("       Factor de Cobertura Frisa Invisible        ")
        print("__________________________________________________")

        # Asegúrate de que el usuario ingrese valores numéricos
        try:
            titulo = float(input("Ingrese titulo de hilado: "))
            longitud_malla = float(input("Ingrese Longitud de Malla: "))
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")
            exit()  # Termina el programa si la entrada no es válida

        factor_frisa = conversion(titulo, longitud_malla)
        print(f"Factor de cobertura Frisa Invisible: {factor_frisa}")

else:
    print("Usuario incorrecto")


def conversion(titulo, longitud_malla):
    paso1 = titulo * float(768)
    paso2 = float(1000) * float(453) / float(paso1)
    resultado = paso2 ** float(0.5)
    return resultado / longitud_malla  # Mover la división aquí para usar longitud_malla en el cálculo
