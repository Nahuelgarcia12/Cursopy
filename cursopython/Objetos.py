# Clase de contacto
class Contacto:

    def inicializar_contacto(self,
        nombre, apellido,
        celular, email):
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.email = email

    def mostrar_contacto(self):
        print(f'''Contacto:
            Nombre: {self.nombre}
            Apellido: {self.apellido}
            Celular: {self.celular}
            Email: {self.email}
        ''')

# Codigo Principal
print('*** Clases y Objetos en Python')
# Crear un primer objeto
contacto1 = Contacto()
contacto1.inicializar_contacto('Agustin', 'Acosta',
                               '11 34538750', 'agusacosta@mail.com')
contacto1.mostrar_contacto()
contacto2 = Contacto()
contacto2.inicializar_contacto('Nahuel', 'Garcia' '',
                               '1159604323','nahug@gmail.com')
contacto2.mostrar_contacto()