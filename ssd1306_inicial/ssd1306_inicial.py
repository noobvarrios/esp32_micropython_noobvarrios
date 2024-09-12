import machine, time
from ssd1306 import SSD1306_I2C
i2c = machine.SoftI2C(sda=machine.Pin(21), scl=machine.Pin(22))
oled = SSD1306_I2C(128, 32, i2c)

oled.fill(1)
oled.show()
oled.fill(0)
oled.show()
time.sleep(1)
oled.text('Hello', 0, 0)
oled.text('World', 0, 10)
oled.show()
