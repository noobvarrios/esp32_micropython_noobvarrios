#3. Lectura de Botones b. Lectura de entradas. 
from machine import Pin, Timer
import time

sw1 = Pin(8,Pin.IN)
sw2 = Pin(26,Pin.IN)

def switches(a):
    print("sw1: ", sw1.value())
    print("sw2: ", sw2.value())

tim1 = Timer()
tim1.init(period=1000, mode=Timer.PERIODIC, callback=switches)

