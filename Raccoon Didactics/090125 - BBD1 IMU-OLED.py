from machine import Pin, SoftI2C
import time
import ssd1306
from IMU_Libreria import MPU6050  

# Configuración del MPU6050
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)  # Cambia los pines SCL y SDA según tu configuración
mpu = MPU6050(i2c)
led = Pin(2, Pin.OUT)

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

def medirAngulo(ax, ay, az):
    from math import atan2, sqrt, degrees  # Importar funciones necesarias aquí
    roll = degrees(atan2(ay, sqrt(ax**2 + az**2)))
    pitch = degrees(atan2(-ax, sqrt(ay**2 + az**2)))
    return roll, pitch

def obtener_datos_mpu():
    ax, ay, az = mpu.accel.x, mpu.accel.y, mpu.accel.z
    gx, gy, gz = mpu.gyro.x, mpu.gyro.y, mpu.gyro.z
    
    # Calcular ángulos
    roll, pitch = medirAngulo(ax, ay, az)
    
    # Formato de los mensajes para mostrar
    mensaje = f"Roll: {roll:.2f}°\nPitch: {pitch:.2f}°"
    return mensaje

# Bucle principal para leer los datos periódicamente
while True:
    datos_mpu = obtener_datos_mpu()
    
    # Mostrar datos en consola
    print(datos_mpu)
    
    # Mostrar datos en la pantalla OLED
    oled.fill(0)  # Limpia la pantalla
    oled.text("MPU6050 Data:", 0, 0)  # Título
    oled.text(datos_mpu.split('\n')[0], 0, 20)  # Primera línea: Roll
    oled.text(datos_mpu.split('\n')[1], 0, 40)  # Segunda línea: Pitch
    oled.show()  # Actualiza la pantalla OLED
    
    # Control del LED
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(0.5)
