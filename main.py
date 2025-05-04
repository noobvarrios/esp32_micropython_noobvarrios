from machine import Pin, PWM, Timer
import time
import random
import machine
from ssd1306 import SSD1306_I2C
import framebuf

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

i2c = machine.SoftI2C(sda=machine.Pin(21), scl=machine.Pin(22))
oled = SSD1306_I2C(128,32, i2c)

tim1 = Timer(1)



def blackboxD1():
    with open("blackboxD1.pbm", 'rb') as f: #read binary
        f.readline()
        f.readline()
        data = bytearray(f.read())
        fbuf = framebuf.FrameBuffer(data, 128,32, framebuf.MONO_HLSB) #ancho, alto, formato. 
        oled.blit(fbuf,0, 0)
        oled.show()
    
def tocar_mario_y_barrido():
    blackboxD1()
    for _ in range(3):
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

def main(a):
    led = random.choice(leds)
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)

blackboxD1()
tim1.init(period=1000, mode=Timer.PERIODIC, callback=main)
