from machine import Pin, SPI
import time

hspi = SPI(1, 10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23))
cs = Pin(2, Pin.OUT)

def configurar_MAX7219():
    cs.off()
    hspi.write(b'\x09\xFF')  #DECODE MODE
    cs.on()

    cs.off()
    hspi.write(b'\x0A\x00')  #Intensity
    cs.on()

    cs.off()
    hspi.write(b'\x0B\x07') 
    cs.on()

    cs.off()
    hspi.write(b'\x0C\x01')  
    cs.on()

    cs.off()
    hspi.write(b'\x0F\x00')  
    cs.on()


def mostrar_numero(numero):
    for i in range(1, 9):
        cs.off()
        hspi.write(bytes([i, numero % 10])) 
        cs.on()
        numero //= 10 

configurar_MAX7219()

contador = 0

while True:
    mostrar_numero(contador)
    contador += 1
    if contador > 99999999: 
        contador = 0
    time.sleep(1)  
