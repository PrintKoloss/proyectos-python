dato = False
contador = 0

usuario = (input('ingresar usuario: '))

base_usuarios = ["pepe", "juan", "texto"]

while usuario in base_usuarios:

    dato = True

    contador = contador + 1

    if contador>1:
        break


if dato:
    print('Calculo FC para Jersey y Frisa invisible')

    print('____________________________________________')

    print('''Opciones:

        1. Jersey
        2. Frisa Invisible''')

    print('''eh''')
             if(1)
                 break


eleccion = int(input('''Ingresar el articulo que desea calcular FC: '''))



if eleccion == 1 and dato:

    print('--------------------------------------------------')
    print('            Factor de Cobertura Jersey            ')
    print('__________________________________________________')

    titulo = float(input('Ingrese titulo de hilado: '))

    longitud_malla = float(input('Ingrese Longitud de Malla: '))

elif eleccion and dato == 2:

    print('--------------------------------------------------')
    print('       Factor de Cobertura Frisa Invisible        ')
    print('__________________________________________________')

    titulo = float(input('Ingrese titulo de hilado: '))

    longitud_malla = float(input('Ingrese Longitud de Malla: '))
else:
    print('Usuario incorrecto')


def conversion(titulo):

    paso1 = titulo * float(768)

    paso2 = float(1000) * float(453) / float(paso1)

    resultado = paso2 ** float(0.5)

    return resultado

print('___________________________________________________')

factor_jersey = conversion(titulo) / longitud_malla


print(f'Factor de cobertura: {factor_jersey}')





