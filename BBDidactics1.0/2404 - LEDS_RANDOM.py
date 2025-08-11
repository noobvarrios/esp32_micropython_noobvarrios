#2. Diodos LED - d. Parpadeos aleatorios. 

from machine import Pin
import time
import random

leds = [
    Pin(33, Pin.OUT),
    Pin(32, Pin.OUT),
    Pin(25, Pin.OUT),
    Pin(16, Pin.OUT),
    Pin(26, Pin.OUT),
    Pin(17, Pin.OUT),
    Pin(27, Pin.OUT),
    Pin(23, Pin.OUT)
]

while True:
    led = random.choice(leds)
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.1)
