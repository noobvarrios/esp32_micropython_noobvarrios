# Guarda como 'receptor_lora_mejorado.py'
from machine import Pin, SPI
import ulora
import time

# Configuración del receptor
SPI_PINS = (0, 18, 19, 16)  # SPI1, SCK=GP18, MOSI=GP19, MISO=GP16
CS_PIN = 17 # NSS - CS
IRQ_PIN = 28  # DIO0
RESET_PIN = 21  # RST
THIS_ADDRESS = 0x02  # Dirección diferente para receptor

# Inicializar LoRa
lora = ulora.LoRa(
    spi_channel=SPI_PINS,
    interrupt=IRQ_PIN,
    this_address=THIS_ADDRESS,
    cs_pin=CS_PIN,
    reset_pin=RESET_PIN,
    freq=915.0,
    tx_power=14,
    modem_config=ulora.ModemConfig.Bw125Cr45Sf128,
    receive_all=True,
    acks=False
)

print("📡 Receptor LoRa mejorado iniciado")
print("   Frecuencia: 915 MHz")
print("   Esperando datos cada 10 segundos...")
print("="*50)

def parse_sensor_data(message):
    """Parsear el mensaje de datos de sensores"""
    try:
        parts = message.split('|')
        result = {'counter': parts[0].replace('#', '')}
        
        for part in parts[1:]:
            if part.startswith('A'):  # AHT20
                values = part[1:].split(',')
                result['aht20_temp'] = float(values[0])
                result['aht20_hum'] = float(values[1])
            elif part.startswith('B'):  # BMP280
                values = part[1:].split(',')
                result['bmp280_temp'] = float(values[0])
                result['bmp280_pres'] = float(values[1])
                result['bmp280_hum'] = float(values[2])
            elif part.startswith('M'):  # MPU6050
                values = part[1:].split(',')
                result['accel_x'] = float(values[0])
                result['accel_y'] = float(values[1])
                result['accel_z'] = float(values[2])
                result['gyro_x'] = float(values[3])
                result['gyro_y'] = float(values[4])
                result['gyro_z'] = float(values[5])
                result['mpu_temp'] = float(values[6])
            elif part.startswith('T'):  # Timestamp
                result['timestamp'] = part[1:]
        
        return result
    except Exception as e:
        print(f"Error parseando mensaje: {e}")
        return None

def receive_callback(payload):
    """Manejar mensajes recibidos"""
    try:
        message = payload.decode()
        data = parse_sensor_data(message)
        
        if data:
            print(f"\n📩 Mensaje #{data['counter']} recibido")
            print(f"   📍 Desde: 0x{payload.header_from:02X}")
            print(f"   📶 RSSI: {lora.get_rssi():.1f} dBm")
            print(f"   📊 SNR: {lora.get_snr():.1f} dB")
            
            if 'aht20_temp' in data:
                print(f"   🌡️  AHT20: {data['aht20_temp']:.1f}°C, {data['aht20_hum']:.1f}%")
            
            if 'bmp280_temp' in data:
                print(f"   🌀 BMP280: {data['bmp280_temp']:.1f}°C, {data['bmp280_pres']:.1f}hPa, {data['bmp280_hum']:.1f}%")
            
            if 'accel_x' in data:
                print(f"   📍 MPU6050: A({data['accel_x']:.2f},{data['accel_y']:.2f},{data['accel_z']:.2f}g)")
                print(f"               G({data['gyro_x']:.1f},{data['gyro_y']:.1f},{data['gyro_z']:.1f}°/s)")
                print(f"               T({data['mpu_temp']:.1f}°C)")
            
            print("-" * 50)
        else:
            print(f"📦 Mensaje crudo: {message}")
            
    except Exception as e:
        print(f"❌ Error procesando mensaje: {e}")

# Configurar callback
lora.on_receive(receive_callback)
lora.set_mode_rx()

print("✅ Receptor listo. Esperando datos...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n🛑 Receptor detenido")
    lora.set_mode_sleep()