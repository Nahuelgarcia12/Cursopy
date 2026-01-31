print('*** Anexar informacion a un archivo ***')
archivo = open('mi_archivo.txt', 'a')  # append - anexar
archivo.write('Anexando informacion...\n')
archivo.write('Saliendo de anexar informacion...\n')
archivo.close()