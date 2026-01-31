import os

# Escribir una lista de datos a un archivo

nombre_archivo = 'mi_archivo.txt'
lista = ['Global\n', 'Mentoring\n']
with open(nombre_archivo, 'a+') as archivo:# tambienn esta modo w+ y r+
    archivo.writelines(lista)
print('Se anexo la lista de datos')

# Eliminar un archivo
if os.path.exists(nombre_archivo):
    os.remove(nombre_archivo)
    print(f'Se elimino el archivo : {nombre_archivo}')
else:
    print(f'Archivo no encontrado: {nombre_archivo}')

