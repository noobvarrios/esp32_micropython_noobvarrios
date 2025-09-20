from machine import Pin, I2C
import time
from ahtx0 import AHT20
from bme280_float import BME280

# Intentar importar MPU6050, si no existe la librería no falla
try:
    from mpu6050 import MPU6050
    HAS_MPU = True
except ImportError:
    print("⚠️ Librería 'mpu6050' no encontrada, se omitirá este sensor")
    HAS_MPU = False


class SensorStation:
    def __init__(self):
        # Actualizado: SCL=GPIO5, SDA=GPIO4
        self.i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
        self.sensors = {}
        self.initialize_sensors()
    
    def initialize_sensors(self):
        print("Inicializando sensores con nuevos pines...")
        print("SCL: GPIO5, SDA: GPIO4")
        print("Dispositivos I2C detectados:", [hex(addr) for addr in self.i2c.scan()])
        
        # Inicializar AHT20
        try:
            self.sensors['aht20'] = AHT20(self.i2c)
            print("✓ AHT20 listo")
        except Exception as e:
            print("✗ AHT20 error:", e)
        
        # Inicializar BMP280
        try:
            self.sensors['bmp280'] = BME280(i2c=self.i2c, address=0x77)
            print("✓ BMP280 listo")
        except Exception as e:
            print("✗ BMP280 error:", e)
        
        # Inicializar MPU6050 solo si la librería está disponible
        if HAS_MPU:
            try:
                self.sensors['mpu6050'] = MPU6050(self.i2c)
                # Test rápido para verificar que funciona
                temp = self.sensors['mpu6050'].temperature()
                print(f"✓ MPU6050 listo (Temp inicial: {temp:.1f}°C)")
            except Exception as e:
                print("✗ MPU6050 error:", e)
    
    def read_all(self):
        data = {}
        
        # Leer AHT20
        if 'aht20' in self.sensors:
            try:
                data['aht20_temp'] = self.sensors['aht20'].temperature
                data['aht20_hum'] = self.sensors['aht20'].relative_humidity
            except:
                data['aht20_error'] = True
        
        # Leer BMP280
        if 'bmp280' in self.sensors:
            try:
                t, p, h = self.sensors['bmp280'].values
                data['bmp280_temp'] = t
                data['bmp280_pres'] = p
                data['bmp280_hum'] = h
            except:
                data['bmp280_error'] = True
        
        # Leer MPU6050 - ¡MÉTODOS CORREGIDOS!
        if 'mpu6050' in self.sensors:
            try:
                # Usar los métodos correctos de tu librería
                accel_tuple = self.sensors['mpu6050'].acceleration()
                gyro_tuple = self.sensors['mpu6050'].gyro()
                
                # Convertir a diccionario para consistencia
                data['mpu_accel'] = {
                    'x': accel_tuple[0],
                    'y': accel_tuple[1], 
                    'z': accel_tuple[2]
                }
                data['mpu_gyro'] = {
                    'x': gyro_tuple[0],
                    'y': gyro_tuple[1],
                    'z': gyro_tuple[2]
                }
                data['mpu_temp'] = self.sensors['mpu6050'].temperature()
            except Exception as e:
                print(f"Error leyendo MPU6050: {e}")
                data['mpu_error'] = True
        
        return data
    
    def print_data(self, data):
        print("\n" + "="*50)
        print("ESTACIÓN DE SENSORES - DATOS COMPLETOS")
        print("="*50)
        
        # AHT20
        if 'aht20_temp' in data:
            print("AHT20    -> Temp: {:.1f}°C, Hum: {:.1f}%".format(data['aht20_temp'], data['aht20_hum']))
        elif 'aht20_error' in data:
            print("AHT20    -> Error de lectura")
        
        # BMP280
        if 'bmp280_temp' in data:
            print("BMP280   -> Temp: {}, Pres: {}, Hum: {}".format(
                data['bmp280_temp'], data['bmp280_pres'], data['bmp280_hum']))
        elif 'bmp280_error' in data:
            print("BMP280   -> Error de lectura")
        
        # MPU6050
        if 'mpu_accel' in data:
            accel = data['mpu_accel']
            gyro = data['mpu_gyro']
            print("MPU6050  -> Accel: X={:.2f}g, Y={:.2f}g, Z={:.2f}g".format(accel['x'], accel['y'], accel['z']))
            print("           Gyro:  X={:.1f}°/s, Y={:.1f}°/s, Z={:.1f}°/s".format(gyro['x'], gyro['y'], gyro['z']))
            print("           Temp: {:.1f}°C".format(data['mpu_temp']))
        elif 'mpu_error' in data:
            print("MPU6050  -> Error de lectura")
        
        print("="*50)


# Uso principal
station = SensorStation()
counter = 0

while True:
    counter += 1
    print(f"\nLectura #{counter}")
    sensor_data = station.read_all()
    station.print_data(sensor_data)
    time.sleep(3)