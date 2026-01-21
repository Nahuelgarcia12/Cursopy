class Animal:
    def comer(self):
        print('Como muchas veces al dia')

    def dormir(self):
        print('Duermo muchas horas')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

    def dormir(self):
        print('Duermo 15 horas al dia')

print('*** Ejemplo Herencia en Python ***')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()
#animal1.hacer_sonido() manda error, metodo de la clase hija

print('\nClase Hija, soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir() # Sobreescrito
perro1.hacer_sonido()
