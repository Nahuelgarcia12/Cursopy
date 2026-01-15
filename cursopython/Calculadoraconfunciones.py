# Reto Calculadora con funciones
print(f'*** Calculadora con Funciones ***')

def mostrar_menu():
    print('''Operaciones que puedes realizar:
    1. Suma
    2. Resta 
    3. Multiplicacion
    4. Division
    5. Salir''')
    opcion = int(input('Escoje una opcion: '))
    return opcion

def pedir_valores():
    op1 = float(input('Dame el valor 1: '))
    op2 = float(input('Dame el valor 2: '))
    return op1, op2

def ejecutar_operacion(opcion, salir):
    # Solicitamos en primer lugar los valores de los operandos
    global operando1, operando2
    if 1 <= opcion <= 4:
        operando1, operando2 = pedir_valores()
    resultado = 0
    if opcion == 1:  # Suma
        resultado = operando1 + operando2
        print(f'El resultado de la suma es: {resultado}\n')
    elif opcion == 2:  # Resta
        resultado = operando1 - operando2
        print(f'El resultado de la resta es: {resultado}\n')
    elif opcion == 3:  # Multiplicacion
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicacion es: {resultado}\n')
    elif opcion == 4:  # Division
        resultado = operando1/operando2
        print(f'El resultado de la division es: {resultado}\n')
    elif opcion == 5:  # Salir
        print('Saliendo del programa Calculadora. Hasta pronto...')
        salir = True
    else:
        print('Opcion invalida, selecciona otra opcion...\n')

    return salir

# Codigo principal
salir = False
while not salir:
    opcion = mostrar_menu()
    salir = ejecutar_operacion(opcion, salir)