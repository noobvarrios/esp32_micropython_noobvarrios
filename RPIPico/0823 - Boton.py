#3. Lectura de Botones b. Lectura de entradas. 
from machine import Pin, Timer
import time

btnazul = Pin(6,Pin.IN)
btnrojo = Pin(7,Pin.IN)

def botones(a):
    print("Boton AZUL: ", btnazul.value())
    print("Boton ROJO: ", btnrojo.value())

tim1 = Timer()
tim1.init(period=1000, mode=Timer.PERIODIC, callback=botones)
