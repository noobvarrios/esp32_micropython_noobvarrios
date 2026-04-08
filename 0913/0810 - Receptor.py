from machine import Pin
import time
import ulora

# Pines según tu conexión
SPI_PINS = (0, 18, 19, 16)  # SPI0, SCK=GP18, MOSI=GP19, MISO=GP16
CS_PIN = 17               # GP5
IRQ_PIN = 28            # Cambia si tu DIO0 está en otro pin
RESET_PIN = 21            # Cambia si tu RST está en otro pin

# Dirección de este nodo
THIS_ADDRESS = 255  # Receptor universal

# Crear objeto LoRa
lora = ulora.LoRa(
    spi_channel=SPI_PINS,                     # Tupla personalizada
    interrupt=IRQ_PIN,
    this_address=THIS_ADDRESS,
    cs_pin=CS_PIN,
    reset_pin=RESET_PIN,
    freq=915.0,                               # MHz
    tx_power=14,
    modem_config=ulora.ModemConfig.Bw125Cr45Sf128,
    receive_all=True,
    acks=False
)

# Definir función para manejar recepción
def on_receive(payload):
    try:
        msg = payload.message.decode('utf-8')
    except:
        msg = str(payload.message)
    print(f"Desde {payload.header_from}: {msg} | RSSI={payload.rssi} dBm | SNR={payload.snr} dB")

lora.on_recv = on_receive
lora.set_mode_rx()

print("Receptor LoRa iniciado en 915 MHz...")

while True:
    time.sleep(0.1)  # El manejo de paquetes lo hace la IRQ
