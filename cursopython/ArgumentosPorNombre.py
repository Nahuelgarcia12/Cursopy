print('*** Funcion con argumentos por nombre ***')

def crear_persona(nombre, apellido='', edad=0):
    print(f'Persona: nombre = {nombre}, apellido: {apellido}, edad: {edad}')

# Llamamos a la funcion
#crear_persona('Ricardo')

# llamar a la funcion argumentos por nombre
crear_persona(edad=29, nombre='Ricardo')