#2. Diodos LED - a. Secuencia de Luces.
from machine import Pin
import time

# LEDs en orden de serpiente
leds = [
    Pin(27, Pin.OUT),  # Azul 1
    Pin(23, Pin.OUT),  # Azul 2
    Pin(26, Pin.OUT),  # Rojo 1
    Pin(17, Pin.OUT),  # Rojo 2
    Pin(25, Pin.OUT),  # Amarillo 1
    Pin(16, Pin.OUT),  # Amarillo 2
    Pin(33, Pin.OUT),  # Verde 1
    Pin(32, Pin.OUT)   # Verde 2
]

while True:
    # Encender LEDs uno a uno
    for led in leds:
        led.on()
        time.sleep(0.1)
    
    # Apagar LEDs uno a uno (en el mismo orden)
    for led in leds:
        led.off()
        time.sleep(0.1)
