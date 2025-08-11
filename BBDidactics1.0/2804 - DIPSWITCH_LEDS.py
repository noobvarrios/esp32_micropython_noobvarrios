#4. Control Binario c. Generacion de eventos con combinaciones dip-switch. 
from machine import Pin, Timer
import time

dip1 = Pin(4, Pin.IN, Pin.PULL_UP)
dip2 = Pin(5, Pin.IN, Pin.PULL_UP)
dip3 = Pin(18, Pin.IN, Pin.PULL_UP)
dip4 = Pin(19, Pin.IN, Pin.PULL_UP)

led4 = Pin(33, Pin.OUT)
led8 = Pin(32, Pin.OUT)

led3 = Pin(25, Pin.OUT)
led7 = Pin(16, Pin.OUT)

led2 = Pin(26, Pin.OUT)
led6 = Pin(17, Pin.OUT)

led1 = Pin(27, Pin.OUT)
led5 = Pin(23, Pin.OUT)

def dip_leds(a): 
    if dip1.value() == 0:
        led4.on()
        led8.on()
    else:
        led4.off()
        led8.off()

    if dip2.value() == 0:
        led3.on()
        led7.on()
    else:
        led3.off()
        led7.off()

    if dip3.value() == 0:
        led2.on()
        led6.on()
    else:
        led2.off()
        led6.off()

    if dip4.value() == 0:
        led1.on()
        led5.on()
    else:
        led1.off()
        led5.off()
        
        
tim1 = Timer(1)
tim1.init(period=1000, mode=Timer.PERIODIC, callback=dip_leds)

