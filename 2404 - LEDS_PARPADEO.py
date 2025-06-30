#2. Diodos LED - c. Parpadeos Sincronizados.
from machine import Pin
import time

#VERDES
led4 = Pin(33, Pin.OUT)
led8 = Pin(32, Pin.OUT)

#AMARILLO
led3 = Pin(25, Pin.OUT)
led7 = Pin(16, Pin.OUT)

#ROJO
led2 = Pin(26, Pin.OUT)
led6 = Pin(17, Pin.OUT)

#AZUL
led1 = Pin(27, Pin.OUT)
led5 = Pin(23, Pin.OUT)

while True:
    led8.on()
    led4.on()
    led3.on()
    led2.on()
    led1.on()
    led6.on()
    led7.on()
    led5.on()
    
    time.sleep(1)
    #VERDES
    led8.off()
    led4.off()
    #AMARILLOS
    led3.off()
    led7.off()
    #ROJOS
    led2.off()
    led6.off()
    #AZULES
    led1.off()
    led5.off()    
    time.sleep(1)

