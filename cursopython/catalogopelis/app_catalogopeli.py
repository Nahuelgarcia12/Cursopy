
from pelicula import Pelicula
from catalogo_peliculas import CatalogoPeliculas as catalogo_peliculas

print("##App Catalogo de Peliculas##")
opcion = None

while opcion != 4:
    try:
        print('''opciones:
        1.agregar Pelicula
        2. listar Pelicula
        3.Eliminar Pelicula
        4.Salir''')

        opcion = int(input('escribe una opcion (1-4): '))

        if opcion == 1:
            nombre_pelicula = input('ingresa el nombre del Pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            catalogo_peliculas.agregar_pelicula(pelicula)

        elif opcion == 2:
            catalogo_peliculas.listar_peliculas()

        elif opcion == 3:
            catalogo_peliculas.eliminar_        peliculas()

    except Exception as e:
        print(f'ocurrio un error :{e}')
        opcion = None

else:
    print('salimos del programa')

