# Guarda como 'receptor_lora_compatible.py'
from machine import Pin, SPI
import ulora
import time

# Configuración del receptor con nuevos pines
SPI_PINS = (0, Pin(18), Pin(19), Pin(16))  # SCK=GPIO18, MOSI=GPIO19, MISO=GPIO16
IRQ_PIN = Pin(28)     # DIO0 → GPIO28
CS_PIN = Pin(17)      # NSS → GPIO17
RESET_PIN = Pin(21)   # RESET → GPIO21
THIS_ADDRESS = 0x02   # Dirección diferente para receptor

# Variable global para almacenar mensajes recibidos
received_messages = []

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

def on_receive_callback(payload):
    """Callback para manejar mensajes recibidos"""
    global received_messages
    try:
        message = payload.message.decode()
        received_messages.append({
            'message': message,
            'from': payload.header_from,
            'rssi': payload.rssi,
            'snr': payload.snr,
            'time': time.ticks_ms()
        })
    except Exception as e:
        print(f"Error en callback: {e}")

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

# Configurar el callback de recepción
lora.on_recv = on_receive_callback

print("📡 Receptor LoRa Compatible")
print("   SPI: SCK=GPIO18, MOSI=GPIO19, MISO=GPIO16")
print("   Control: CS=GPIO17, RST=GPIO21, DIO0=GPIO28")
print("   Frecuencia: 915 MHz")
print("   Esperando datos...")
print("="*50)

# Poner en modo recepción continua
lora.set_mode_rx()
print("✅ Receptor listo. Esperando datos...")

try:
    last_processed = 0
    while True:
        # Procesar mensajes recibidos
        if received_messages and time.ticks_ms() - last_processed > 100:
            msg_data = received_messages.pop(0)
            
            data = parse_sensor_data(msg_data['message'])
            
            if data:
                print(f"   📩 Mensaje #{data['counter']} recibido")
                print(f"   📍 Desde: 0x{msg_data['from']:02X}")
                print(f"   📶 RSSI: {msg_data['rssi']:.1f} dBm")
                print(f"   📊 SNR: {msg_data['snr']:.1f} dB")
                
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
                print(f"📦 Mensaje crudo: {msg_data['message']}")
            
            last_processed = time.ticks_ms()
        
        time.sleep(0.1)  # Pequeña pausa
        
except KeyboardInterrupt:
    print("\n🛑 Receptor detenido")
    lora.set_mode_sleep()