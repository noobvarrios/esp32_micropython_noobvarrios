from machine import Pin, Timer

led = Pin(25, Pin.OUT)

def parpa(timer):
    led.toggle()

timer = Timer()
timer.init(freq=2.0, mode=Timer.PERIODIC, callback=parpa)
