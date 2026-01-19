class Persona:
    # Constructor
    def __init__(self, nombre, apellido,telefono):
        self._nombre = nombre  # Atributo protegido
        self.__apellido = apellido  # Atributo privado
        self.telefono = telefono #atributo publico

    def mostrar_persona(self):
        print(f'Persona: nombre = {self._nombre}, apellido = {self.__apellido}, telefono = {self.telefono}')

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

# Codigo Principal
persona1 = Persona('Esteban', 'Quiroz', 1150976542)
#persona1.mostrar_persona()

# Lectura de los atributos
print(persona1.get_nombre())
print(persona1.get_apellido())
print(persona1.get_telefono())

# Modificar los valores de los atributos
persona1.set_nombre('Juan')
persona1.set_apellido('Riqulme')
persona1.mostrar_persona()


