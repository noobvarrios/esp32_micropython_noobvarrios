# mpu6050.py - Guarda este código como un nuevo archivo
import machine
import time

class MPU6050:
    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr
        # Wake up the sensor
        self.i2c.writeto_mem(self.addr, 0x6B, b'\x00')
        time.sleep(0.1)
        
    def whoami(self):
        return self.i2c.readfrom_mem(self.addr, 0x75, 1)[0]
    
    def acceleration(self):
        data = self.i2c.readfrom_mem(self.addr, 0x3B, 6)
        x = (data[0] << 8 | data[1]) / 16384.0
        y = (data[2] << 8 | data[3]) / 16384.0
        z = (data[4] << 8 | data[5]) / 16384.0
        return (x, y, z)
    
    def gyro(self):
        data = self.i2c.readfrom_mem(self.addr, 0x43, 6)
        x = (data[0] << 8 | data[1]) / 131.0
        y = (data[2] << 8 | data[3]) / 131.0
        z = (data[4] << 8 | data[5]) / 131.0
        return (x, y, z)
    
    def temperature(self):
        data = self.i2c.readfrom_mem(self.addr, 0x41, 2)
        temp_raw = (data[0] << 8 | data[1])
        temp_c = (temp_raw / 340.0) + 36.53
        return temp_c