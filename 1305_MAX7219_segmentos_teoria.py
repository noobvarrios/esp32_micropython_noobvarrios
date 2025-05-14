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
    hspi.write(b'\x0B\x07') #SCAN LIMIT CANTIDAD DE REGISTROS DISPONIBLES
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

def limpiar_display():
    for i in range(1, 9):  # Hay 8 dígitos (1 a 8)
        cs.off()
        hspi.write(bytes([i, 0x00]))  # Apaga todos los segmentos del dígito
        cs.on()
        
configurar_MAX7219()
# limpiar_display()

segmentos = {
    'A': 0b01000000,
    'B': 0b00100000,
    'C': 0b00010000,
    'D': 0b00001000,
    'E': 0b00000100,
    'F': 0b00000010,
    'G': 0b00000001,
    'DP': 0b10000000,
}

for i in range (1,100,1):
    for nombre, valor in segmentos.items():
        for i in range(1, 9):
            cs.off()
            hspi.write(bytes([i, valor]))
            cs.on()
        print("Segmento encendido:", nombre)
        time.sleep(1)
    