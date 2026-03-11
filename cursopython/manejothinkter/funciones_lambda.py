# Una funcion lambda es una funcion anonima y de una sola linea

# Ej. una funcion normal
def sumar(a, b):
  return a + b

print(sumar(10, 20))

# Funcion lambda
sumar_lambda = lambda a, b: a + b

# Llamamos a la funcion lambda (callback)
print(sumar_lambda(10, 4))