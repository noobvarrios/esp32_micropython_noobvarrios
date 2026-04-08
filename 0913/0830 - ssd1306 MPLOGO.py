#14. Using a SSD1306 OLED oled
#https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html

#5.Visualizacion de datos. c.Introduccion al manejo de archivos con Python. 

import machine
from ssd1306 import SSD1306_I2C
import framebuf
import time

i2c = machine.SoftI2C(sda=machine.Pin(4), scl=machine.Pin(5))
oled = SSD1306_I2C(128,32, i2c)

oled.fill(0)
oled.fill_rect(0, 0, 32, 32, 1)
oled.fill_rect(2, 2, 28, 28, 0)
oled.vline(9, 8, 22, 1)
oled.vline(16, 2, 22, 1)
oled.vline(23, 8, 22, 1)
oled.fill_rect(26, 24, 2, 4, 1)
oled.text('MicroPython', 40, 0, 1)
oled.text('SSD1306', 40, 12, 1)
oled.text('OLED 128x64', 40, 24, 1)
oled.show()

