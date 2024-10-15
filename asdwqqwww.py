dato = False
contador = 0
usuario = input('ingresar usuario: ')

base_usuarios = ["pepe", "juan", "texto"]

# while (contador == 0):
while usuario in base_usuarios:

    dato = True

    contador = contador + 1

    if contador>1:
        break



if dato:

    print('--------------------------------------------------')
    print('      Calculo de Factor de Cobertura Jersey       ')
    print('__________________________________________________')

    titulo = float(input('Ingrese titulo de hilado: '))

    longitud_malla = float(input('Ingrese Longitud de Malla: '))

else:
    print('usuario incorrecto')


def conversion(titulo):

    paso1 = titulo * float(768)

    paso2 = float(1000) * float(453) / float(paso1)

    resultado = paso2 ** float(0.5)

    return resultado

print('___________________________________________________')

factor = conversion(titulo) / longitud_malla


print(f'Factor de cobertura: {factor}')



