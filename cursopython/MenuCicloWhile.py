# Menu interactivo con ciclo while
print('*** Sistema Bancario NG')
salir = False
saldo = 5000
ret = 0
deposito = 0

while not salir:
    print(f'''Menu:
        1. Consultar saldo
        2. Retirar saldo
        3. Depositar saldo
        4. Salir''')

    opcion = int(input('Escoje una opcion: '))

    if opcion == 1:
        print(f'Su saldo es: $ {saldo:.2f}\n')

    elif opcion == 2:
        ret = int(input('Escoja cuanto saldo desea retirar: '))
        if ret <= saldo:
            saldo -= ret
            print(f'El saldo nuevo es: ${saldo:.2f}\n')
        else:
            print(f'Opción inválida, usted no cuenta con ese monto. Su saldo es ${saldo:.2f}\n')

    elif opcion == 3:
        deposito = int(input('Escoja cuanto saldo desea depositar: '))
        saldo += deposito
        print(f'Su saldo nuevo es: ${saldo:.2f}\n')

    elif opcion == 4:
        print('Saliendo del sistema. Hasta pronto ...\n')
        salir = True

    else:
        print('Opción inválida, selecciona otra opción...\n')
