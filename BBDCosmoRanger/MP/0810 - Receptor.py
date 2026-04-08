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
SPI_PINS = (0, 18, 19, 16)  # SPI0, SCK=GP18, MOSI=GP19, MISO=GP16
CS_PIN = 17 # NSS - CS
IRQ_PIN = 28  # DIO0
RESET_PIN = 21  # RST

#nodo
THIS_ADDRESS = 255  # Receptor universal

#objeto lora de la libreria 
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

"""
MENSAJES BRANDON
MPY: soft reboot
Receptor LoRa iniciado en 915 MHz...
Desde 1: Mensaje #1 desde Pico | RSSI=-97.27 dBm | SNR=9.25 dB
Desde 1: Mensaje #3 desde Pico | RSSI=-91.93 dBm | SNR=9.5 dB
Desde 1: Mensaje #5 desde Pico | RSSI=-91.93 dBm | SNR=10.0 dB
Desde 1: Mensaje #7 desde Pico | RSSI=-95.13 dBm | SNR=9.5 dB
Desde 1: Mensaje #9 desde Pico | RSSI=-87.67 dBm | SNR=9.25 dB
Desde 1: Mensaje #11 desde Pico | RSSI=-87.67 dBm | SNR=9.5 dB
Desde 1: Mensaje #13 desde Pico | RSSI=-94.07 dBm | SNR=9.75 dB
Desde 1: Mensaje #15 desde Pico | RSSI=-82.33 dBm | SNR=9.75 dB
Desde 1: Mensaje #17 desde Pico | RSSI=-89.8 dBm | SNR=9.5 dB
Desde 1: Mensaje #19 desde Pico | RSSI=-97.27 dBm | SNR=10.25 dB
Desde 1: Mensaje #21 desde Pico | RSSI=-82.33 dBm | SNR=9.75 dB
Desde 1: Mensaje #23 desde Pico | RSSI=-86.6 dBm | SNR=9.75 dB
Desde 1: Mensaje #25 desde Pico | RSSI=-64.2 dBm | SNR=9.5 dB
Desde 1: Mensaje #27 desde Pico | RSSI=-79.13 dBm | SNR=10.0 dB
Desde 1: Mensaje #29 desde Pico | RSSI=-70.6 dBm | SNR=9.75 dB
Desde 1: Mensaje #31 desde Pico | RSSI=-74.87 dBm | SNR=10.25 dB
Desde 1: Mensaje #33 desde Pico | RSSI=-84.47 dBm | SNR=9.5 dB
Desde 1: Mensaje #35 desde Pico | RSSI=-101.53 dBm | SNR=9.5 dB
Desde 1: Mensaje #37 desde Pico | RSSI=-100.47 dBm | SNR=9.5 dB
Desde 1: Mensaje #39 desde Pico | RSSI=-91.93 dBm | SNR=10.0 dB
Desde 1: Mensaje #41 desde Pico | RSSI=-98.33 dBm | SNR=4.0 dB
Desde 1: Mensaje #43 desde Pico | RSSI=-105.8 dBm | SNR=9.0 dB
Desde 1: Mensaje #45 desde Pico | RSSI=-104.73 dBm | SNR=9.75 dB
Desde 1: Mensaje #47 desde Pico | RSSI=-112.2 dBm | SNR=6.0 dB
Desde 1: Mensaje #49 desde Pico | RSSI=-103.67 dBm | SNR=8.75 dB
Desde 1: Mensaje #53 desde Pico | RSSI=-100.47 dBm | SNR=9.5 dB
Desde 1: Mensaje #55 desde Pico | RSSI=-104.73 dBm | SNR=8.5 dB
Desde 1: Mensaje #57 desde Pico | RSSI=-93.0 dBm | SNR=10.0 dB
Desde 1: Mensaje #59 desde Pico | RSSI=-96.2 dBm | SNR=9.0 dB
Desde 1: Mensaje #61 desde Pico | RSSI=-90.87 dBm | SNR=10.25 dB
Desde 1: Mensaje #63 desde Pico | RSSI=-89.8 dBm | SNR=9.75 dB
Desde 1: Mensaje #65 desde Pico | RSSI=-83.4 dBm | SNR=9.75 dB
Desde 1: Mensaje #67 desde Pico | RSSI=-80.2 dBm | SNR=9.5 dB
Desde 1: Mensaje #69 desde Pico | RSSI=-65.27 dBm | SNR=10.0 dB
Desde 1: Mensaje #71 desde Pico | RSSI=-53.53 dBm | SNR=9.5 dB
Desde 1: Mensaje #73 desde Pico | RSSI=-68.47 dBm | SNR=9.75 dB
Desde 1: Mensaje #75 desde Pico | RSSI=-63.13 dBm | SNR=10.25 dB
Desde 1: Mensaje #77 desde Pico | RSSI=-67.4 dBm | SNR=9.75 dB
Desde 1: Mensaje #79 desde Pico | RSSI=-61.0 dBm | SNR=10.0 dB
Desde 1: Mensaje #81 desde Pico | RSSI=-54.6 dBm | SNR=9.75 dB
Desde 1: Mensaje #83 desde Pico | RSSI=-82.33 dBm | SNR=10.0 dB
"""