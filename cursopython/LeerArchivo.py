print('*** Leer informacion de un Archivo ***')
archivo = open('mi_archivo.txt', 'r')  # read - leer
print(archivo.read()) # lee el arch completo
# print (archivo.readlines()) lee una linea
archivo.close()