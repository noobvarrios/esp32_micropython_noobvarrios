from machine import Pin, PWM
import time
import random

buzzer = PWM(Pin(2))

notas = [
    (660, 0.1), (660, 0.1), (0, 0.1), (660, 0.1),
    (0, 0.1), (520, 0.1), (660, 0.1), (0, 0.1),
    (770, 0.1)
]
pausa = 0.05

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

def tocar_mario_y_barrido():
    for _ in range(2):
        for freq, duracion in notas:
            if freq == 0:
                buzzer.duty(0)
            else:
                buzzer.freq(freq)
                buzzer.duty(512)
            for led in leds:
                led.on()
                time.sleep(duracion / len(leds))
                led.off()
            buzzer.duty(0)
            time.sleep(pausa)
        time.sleep(0.5)

tocar_mario_y_barrido()

while True:
    led = random.choice(leds)
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
