from machine import Pin
from machine import Timer
import time


led = Pin(8, Pin.OUT)
tim1 = Timer()


def parpadeo(t):
    led.toggle()

tim1.init(period=1000, mode=Timer.PERIODIC, callback=parpadeo)

