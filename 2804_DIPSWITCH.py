from machine import Pin, Timer

led4 = Pin(4, Pin.IN, Pin.PULL_UP)
led5 = Pin(5, Pin.IN, Pin.PULL_UP)
led18 = Pin(18, Pin.IN, Pin.PULL_UP)
led19 = Pin(19, Pin.IN, Pin.PULL_UP)

def dip_switch(timer):
    print("Pin 4:", led4.value())
    print("Pin 5:", led5.value())
    print("Pin 18:", led18.value())
    print("Pin 19:", led19.value())
    print("--------------------")

tim1 = Timer(1)
tim1.init(period=1000, mode=Timer.PERIODIC, callback=dip_switch)
