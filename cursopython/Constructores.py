class Persona:
    # Constructor
    def __init__(self, nombre, apellido, telefono):
        self._nombre = nombre #atributo protegidp-
        self.__apellido = apellido #atributo privado
        self.telefono = telefono #atributo publico (se puede modificar)

    def mostrar_persona(self):
        print(f'Persona: nombre = {self.nombre}, apellido = {self.apellido}, telefono = {self.telefono}')


# Codigo Principal
persona1 = Persona('Nahuel', 'Garcia', 115034654)
persona1.mostrar_persona()
