import machine, time
from ssd1306 import SSD1306_I2C

# Configuración de pines (cambia los números si usas otros GPIO)
i2c = machine.SoftI2C(sda=machine.Pin(4), scl=machine.Pin(5))

# Inicializar OLED
oled = SSD1306_I2C(128, 32, i2c)

oled.fill(1)
oled.show()
time.sleep(1)

oled.fill(0)
oled.text('Hello', 0, 0)
oled.text('World', 0, 10)
oled.show()
