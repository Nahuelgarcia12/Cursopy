print('*** Escribir informacion a un archivo ***')
archivo = open('mi_archivo.txt', 'w')  # write - escribir
archivo.write('Hola Mundo\n')
archivo.close()  # Cerramos el buffer