import machine, time
from ssd1306 import SSD1306_I2C

# Inicializar I2C y OLED
i2c = machine.SoftI2C(sda=machine.Pin(4), scl=machine.Pin(5))
oled = SSD1306_I2C(128, 32, i2c)

# Función para dibujar texto en "doble escala"
def draw_big_text(oled, text, x, y, scale=2):
    # Render temporal del carácter
    temp = SSD1306_I2C(128, 32, i2c)
    for i, char in enumerate(text):
        temp.fill(0)
        temp.text(char, 0, 0)
        char_x = x + i * 8 * scale
        for yy in range(8):
            for xx in range(8):
                if temp.pixel(xx, yy):
                    for dy in range(scale):
                        for dx in range(scale):
                            oled.pixel(char_x + xx*scale+dx,
                                       y + yy*scale+dy, 1)

# 1. Mensaje inicial
oled.fill(0)
oled.text("READY TO", 10, 5)
oled.text("LAUNCH", 20, 20)
oled.show()
time.sleep(5)

# 2. Cuenta regresiva 10 → 0
for n in range(10, -1, -1):
    oled.fill(0)
    draw_big_text(oled, str(n), 40, 0, scale=3)
    oled.show()
    time.sleep(1)

# 3. Mensaje final
oled.fill(0)
oled.text("LAUNCHING", 20, 12)
oled.show()
