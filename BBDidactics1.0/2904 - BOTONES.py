#3. Lectura de Botones b. Lectura de entradas. 
from machine import Pin, Timer
import time

btn1 = Pin(35,Pin.IN)
btn2 = Pin(34,Pin.IN)
btn3 = Pin(39,Pin.IN)
btn4 = Pin(36,Pin.IN)

led4 = Pin(33, Pin.OUT)
led8 = Pin(32, Pin.OUT)

led3 = Pin(25, Pin.OUT)
led7 = Pin(16, Pin.OUT)

led2 = Pin(26, Pin.OUT)
led6 = Pin(17, Pin.OUT)

led1 = Pin(27, Pin.OUT)
led5 = Pin(23, Pin.OUT)

def botones(a):
    print("Boton 1: ", btn1.value())
    print("Boton 2: ", btn2.value())
    print("Boton 3: ", btn3.value())
    print("Boton 4: ", btn4.value())
    print("------------------")

    if btn4.value() == 0:
        led4.on()
        led8.on()
    else:
        led4.off()
        led8.off()

    if btn3.value() == 0:
        led3.on()
        led7.on()
    else:
        led3.off()
        led7.off()

    if btn2.value() == 0:
        led2.on()
        led6.on()
    else:
        led2.off()
        led6.off()

    if btn1.value() == 0:
        led1.on()
        led5.on()
    else:
        led1.off()
        led5.off()


tim1 = Timer(1)
tim1.init(period=1000, mode=Timer.PERIODIC, callback=botones)