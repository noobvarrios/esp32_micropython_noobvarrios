from machine import Pin, SPI
import time

hspi = SPI(1, 10000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13))
#SPI(CANAL, VELOCIDAD, MODO SPI, SEÑAL DEL RELOJ, SALIDA DE DATOS)
cs = Pin(15, Pin.OUT)
#CUANDO SE ENVIA UN COMANDO AL MAX7219


"""
cs.off()
hspi.write(bytes([posicion, numero]))
cs.on()
"""
def configurar_MAX7219():
    cs.off()
    #hspi.write(b'\x09\xFF')  #DECODE MODE
    hspi.write(b'\x09\x00') #decode off
    cs.on()

    cs.off()
    hspi.write(b'\x0A\x00')  #BRILLO
    cs.on()

    cs.off()
    hspi.write(b'\x0B\x03') #SCAN LIMIT CANTIDAD DE REGISTROS DISPONIBLES 
    cs.on()

    cs.off()
    hspi.write(b'\x0C\x01')  
    cs.on()

    cs.off()
    hspi.write(b'\x0F\x00')  
    cs.on()


def mostrar_numero(numero):
    for i in range(1, 5): #INDICES DEL DISPLAY
        cs.off() #APAGAMOS EL CS
        hspi.write(bytes([i, numero % 10])) 
        cs.on() #SE CARGA EL DATO. 
        numero //= 10

configurar_MAX7219()

contador = 0

while True:
    cs.off()
    hspi.write(bytes([1,0b01110111]))
    hspi.write(bytes([2,0b10011111]))
    hspi.write(bytes([3,0b01001110]))
    hspi.write(bytes([4,0b00111101]))
    cs.on()
    
    
    
#     mostrar_numero(contador)
#     contador += 2
#     if contador > 99999999: 
#         contador = 0
#     time.sleep(1)  
