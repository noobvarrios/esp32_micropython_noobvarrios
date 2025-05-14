"""
TEORIA: 
    Imagen BPM
    FRAMEBUF [fbuf = framebuf.FrameBuffer(data, 128,32, framebuf.MONO_HLSB) #ancho, alto, formato]
    I2C
    MONO_HLSB???
    
    f.readline()
        f.readline() --> se coloca doble lectura por la estructura de un texto pbm. [TITULO, DIMENSIONES, IMAGEN]
                        SI NO SE LEE DOBLE SE TOMA EL SALTO DE LINEA QUE ESTA EN LAS DIMENSIONES, CORTANDO LA IMAGEN. 
    
"""

from machine import Pin, Timer
import machine
from ssd1306 import SSD1306_I2C
import framebuf
import time

# I2C
i2c = machine.SoftI2C(sda=machine.Pin(21), scl=machine.Pin(22))
oled = SSD1306_I2C(128, 32, i2c)


# VERDE
led4 = Pin(33, Pin.OUT)
led8 = Pin(32, Pin.OUT)
# AMARILLO
led3 = Pin(25, Pin.OUT)
led7 = Pin(16, Pin.OUT)
# ROJO
led2 = Pin(26, Pin.OUT)
led6 = Pin(17, Pin.OUT)
# AZULE
led1 = Pin(27, Pin.OUT)
led5 = Pin(23, Pin.OUT)

def apagar_semaforo():
    for led in [led1, led2, led3, led4, led5, led6, led7, led8]:
        led.value(0)

def semaforo():
    oled.fill(0)
    print("Semáforo vacío")
    with open("semaforo.pbm", 'rb') as f:
        f.readline()
        f.readline()
        data = bytearray(f.read())
    fbuf = framebuf.FrameBuffer(data, 128, 32, framebuf.MONO_HLSB)
    oled.blit(fbuf, 0, 0)
    oled.show()
    apagar_semaforo()  

def rojo():
    oled.fill(0)
    print("Rojo")
    with open("semaforo_rojo.pbm", 'rb') as f:
        f.readline()
        f.readline()
        data = bytearray(f.read())
    fbuf = framebuf.FrameBuffer(data, 128, 32, framebuf.MONO_HLSB)
    oled.blit(fbuf, 0, 0)
    oled.show()
    apagar_semaforo()
    led2.value(1)
    led6.value(1)

def ambar():
    oled.fill(0)
    print("Ámbar")
    with open("semaforo_ambar.pbm", 'rb') as f:
        f.readline()
        f.readline()
        data = bytearray(f.read())
    fbuf = framebuf.FrameBuffer(data, 128, 32, framebuf.MONO_HLSB)
    oled.blit(fbuf, 0, 0)
    oled.show()
    apagar_semaforo()
    led3.value(1)
    led7.value(1)

def verde():
    oled.fill(0)
    print("Verde")
    with open("semaforo_verde.pbm", 'rb') as f:
        f.readline()
        f.readline()
        data = bytearray(f.read())
    fbuf = framebuf.FrameBuffer(data, 128, 32, framebuf.MONO_HLSB)
    oled.blit(fbuf, 0, 0)
    oled.show()
    apagar_semaforo()
    led4.value(1)
    led8.value(1)

for i in range(10):
    semaforo()
    time.sleep(6)
    rojo()
    time.sleep(5)
    ambar()
    time.sleep(2)
    verde()
    time.sleep(4)
