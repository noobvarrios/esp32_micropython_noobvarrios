#5. Visualizacion de datos. f. Visualizacion en pantallas OLED. 

from machine import Pin, SoftI2C, Timer
import machine
import time
from ssd1306 import SSD1306_I2C
from IMU_Libreria import MPU6050   

tim1 = Timer(1)
i2c = machine.SoftI2C(sda=machine.Pin(21), scl=machine.Pin(22))
mpu = MPU6050(i2c)
buzz = Pin(2, Pin.OUT)
ledverde = Pin(33, Pin.OUT)
oled = SSD1306_I2C(128, 32, i2c)


def medirAngulo(ax, ay, az):
    from math import atan2, sqrt, degrees 
    roll = degrees(atan2(ay, sqrt(ax**2 + az**2)))
    pitch = degrees(atan2(-ax, sqrt(ay**2 + az**2)))
    return roll, pitch

def obtener_datos_mpu():
    ax, ay, az = mpu.accel.x, mpu.accel.y, mpu.accel.z
    gx, gy, gz = mpu.gyro.x, mpu.gyro.y, mpu.gyro.z
    
    roll, pitch = medirAngulo(ax, ay, az)
    
    m_roll = f"Roll: {roll:.2f}"
    m_pitch = f"Pitch: {pitch:.2f}"
    return m_roll, m_pitch


while True:
    datos_mpu = obtener_datos_mpu()
    
    print(datos_mpu)
    
    oled.fill(0)  
    oled.text("MPU6050 Data:", 0, 0) 
    oled.text(datos_mpu[0], 0, 10)
    oled.text(datos_mpu[1], 0, 20)  
    oled.show()  
    
    buzz.on()
    ledverde.on()
    time.sleep(1)
    buzz.off()
    ledverde.off()
    time.sleep(0.5)
