class Persona:

    atributo_clase = 0

    def __init__(self):
        self.atributo_instancia = 0

print('*** Atributos de Clase ***')
print(f'Atributo de Clase {Persona.atributo_clase}')
# Modificamos el atributo clase
# (comun a todos los objetos de la clase Persona)
Persona.atributo_clase = 10

# Creamos un objeto
persona1 = Persona()
persona1.atributo_instancia = 20
print(f'Atributo de Clase desde persona1: {persona1.atributo_clase}')
print(f'Atributo de Instancia desde persona1: {persona1.atributo_instancia}')

# Creamos un segundo objeto
persona2 = Persona()
persona2.atributo_instancia = 30
print(f'Atributo de Clase desde persona2: {persona2.atributo_clase}')
print(f'Atributo de Instancia desde persona2: {persona2.atributo_instancia}')

