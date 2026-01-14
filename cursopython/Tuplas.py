from operator import truediv

print('*** Manejo de Tuplas ***')
nombres = ('Pedro', 'Juan', 'Luna')
print(nombres)

# Creamos una tupla heterogenea
tupla_heterogenea = (100, False, 'Ivan')
print(tupla_heterogenea)

# Recorrer los elementos
for nombre in nombres:
   print(nombre, end=' - ')

numeros = (100, 200, 300, 400, 500)
print(f'Para el indice 0, el valor es: {numeros[0]}')
print(f'Para el indice 3, el valor es: {numeros[3]}')
# Con indice negativo se cuenta de derecha a izquierda
print(f'Para el indice -1, el valor es: {numeros[-1]}')
print(f'Para el indice -5, el valor es: {numeros[-5]}')

# No podemos modificar una tupla
# numeros[0] = 1000 manda un error, no podemos modificar elementos de una tupla

numero_a_buscar = 2000
if numero_a_buscar in numeros:
    print(f'Si existe {numero_a_buscar} en la tupla')
else:
    print(f'No existe {numero_a_buscar} en la tupla')


