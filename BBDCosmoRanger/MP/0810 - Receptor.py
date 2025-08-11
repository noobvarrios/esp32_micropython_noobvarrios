"""
Codigo receptor para estacion terrena del CosmoRanger CanSat de BBD
Codigo trabajado en conjunto con IA

Definicion de pines para RPIPICO

LEER LA LIBRERIA PARA COMPRENDER LA TUPLA DE PINES
"""
from machine import Pin
import time
import ulora #Recopilada de https://github.com/martynwheeler/u-lora

#RPI PICO DEFINICION DE PINES
"""
ORDEN DEFINIDIO EN LIBRERIA
self.spi = SPI(self._spi_channel[0], 5000000, sck=Pin(self._spi_channel[1]), mosi=Pin(self._spi_channel[2]), miso=Pin(self._spi_channel[3]))
"""
SPI_PINS = (0, 18, 19, 16)  # SPI1, SCK=GP18, MOSI=GP19, MISO=GP16
CS_PIN = 17 # NSS - CS
IRQ_PIN = 28  # DIO0
RESET_PIN = 22  # RST

# Dirección de este nodo
THIS_ADDRESS = 255  # Receptor universal

# Crear objeto LoRa
lora = ulora.LoRa(
    spi_channel=SPI_PINS, #tupla de pines                
    interrupt=IRQ_PIN,
    this_address=THIS_ADDRESS,
    cs_pin=CS_PIN,
    reset_pin=RESET_PIN,
    freq=915.0, #frecuencia                               
    tx_power=14,
    modem_config=ulora.ModemConfig.Bw125Cr45Sf128,
    receive_all=True,
    acks=False
)

#manejo de recepcion
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
    time.sleep(0.1)  

"""
output
Desde 1: hello 48 | RSSI=-55.67 dBm | SNR=9.75 dB
Desde 1: hello 49 | RSSI=-64.2 dBm | SNR=10.0 dB
Desde 1: hello 50 | RSSI=-59.93 dBm | SNR=9.0 dB
Desde 1: hello 51 | RSSI=-57.8 dBm | SNR=9.5 dB
Desde 1: hello 52 | RSSI=-62.07 dBm | SNR=9.5 dB
Desde 1: hello 53 | RSSI=-61.0 dBm | SNR=9.5 dB
Desde 1: hello 54 | RSSI=-58.87 dBm | SNR=10.25 dB
Desde 1: hello 55 | RSSI=-62.07 dBm | SNR=9.75 dB
Desde 1: hello 56 | RSSI=-64.2 dBm | SNR=10.0 dB
Desde 1: hello 57 | RSSI=-53.53 dBm | SNR=9.75 dB

"""