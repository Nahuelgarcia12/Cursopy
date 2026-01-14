print('*** Manejo de Funciones ***')

# 1. Definir la funcion
def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

# 2. Llamamos a la funcion
numero1 = int(input('numero1 que desea sumar:'))
numero2 = int(input('numero2 que desea sumar: '))
valor_devuelto = sumar(numero1,numero2)
print(f'Valor devuelto de la funcion: {valor_devuelto}')
sumar(numero1,numero2)