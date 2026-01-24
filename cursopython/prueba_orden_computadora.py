from computadora import Computadora
from monitor import Monitor
from orden import Orden
from raton import Raton
from teclado import Teclado

teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', 27)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('Gamer', 'Bluetooth')
raton2 = Raton('Gamer', 'Bluetooth')
monitor2 = Monitor('Gamer', 34)
computadora2 = Computadora('Gamer', monitor2, teclado2, raton2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
#print(orden1)

teclado3 = Teclado('Apple', 'Bluetooth')
raton3 = Raton('Apple', 'Bluetooth')
monitor3 = Monitor('Apple', 27)
computadora3 = Computadora('Apple', monitor3, teclado2, raton1)

orden1.agregar_computadora(computadora3)
print(orden1)