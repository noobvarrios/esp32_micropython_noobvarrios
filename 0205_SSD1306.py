#0205_SSD1306.py

"""
TEORIA: 
    Imagen BPM
    FRAMEBUF [fbuf = framebuf.FrameBuffer(data, 128,32, framebuf.MONO_HLSB) #ancho, alto, formato]
    I2C
    
    
"""

import machine
from ssd1306 import SSD1306_I2C
import framebuf
import time

i2c = machine.SoftI2C(sda=machine.Pin(21), scl=machine.Pin(22))
oled = SSD1306_I2C(128, 32, i2c)

with open("semaforo.pbm", 'rb') as f: #read binary
    f.readline()
    f.readline()
    data = bytearray(f.read())
fbuf = framebuf.FrameBuffer(data, 128,32, framebuf.MONO_HLSB) #ancho, alto, formato. 
oled.blit(fbuf,0, 0)
    
oled.show()

