print('*** Manejo de Set en Python ***')
# Un set es un conjunto de datos NO ordenados
# No se pueden repertir sus elementos
conjunto = {'Pedro', 400, 'Luna', True}
print(conjunto)

#conjunto[0] = 'Karla2' arroja error, no se pueden modificar los elementos

for elemento in conjunto:
   print(elemento, end=' ')

numero_a_buscar = 200
if numero_a_buscar in conjunto:
    print(f'Si existe {numero_a_buscar} en mi set')
else:
    print(f'No existe {numero_a_buscar} en mi set')

largo = len(conjunto)  # length - largo
print(f'La cantidad de elementos en mi set es: {largo}')

# Eliminar un elemento
conjunto.remove(400)
print(conjunto)

# Agregar nuevos elementos
conjunto.add(600)
print(conjunto)