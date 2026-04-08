from machine import Pin, Timer, I2C
import ssd1306

# ---------------------------
# Configuración I2C y pantalla
# ---------------------------
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# ---------------------------
# Definición de botones (GPx)
# ---------------------------
gp2  = Pin(2, Pin.IN)
gp3  = Pin(3, Pin.IN)
gp6  = Pin(6, Pin.IN)
gp7  = Pin(7, Pin.IN)
gp20 = Pin(20, Pin.IN)

# ---------------------------
# Definición de switches (GPx)
# ---------------------------
gp8  = Pin(8, Pin.IN)
gp26 = Pin(26, Pin.IN)

# ---------------------------
# Función de lectura y display
# ---------------------------
def lectura(t):
    oled.fill(0)  # limpiar pantalla

    # Fila 1: GP2, GP3, GP6
    oled.text("2:{} 3:{} 6:{}".format(gp2.value(), gp3.value(), gp6.value()), 0, 0)

    # Fila 2: GP7, GP20
    oled.text("7:{} 20:{}".format(gp7.value(), gp20.value()), 0, 10)

    # Fila 3: GP8, GP26
    oled.text("8:{} 26:{}".format(gp8.value(), gp26.value()), 0, 20)

    oled.show()

# ---------------------------
# Timer para actualizar
# ---------------------------
tim1 = Timer()
tim1.init(period=500, mode=Timer.PERIODIC, callback=lectura)
