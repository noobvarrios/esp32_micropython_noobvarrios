#6. Sonidos c. Uso del Buzzer
"""
En la pipico el rango de duty_u16() es de 16 bits [65,535].
el 50% del ciclo util es 32768
"""
from machine import Pin, PWM
import time

buzzer = PWM(Pin(21))

secuencia = [2000, 2500, 3000, 3500]
duracion_beep = 0.05
pausa_entre = 0.02

while True:
    for freq in secuencia:
        buzzer.freq(freq)
        buzzer.duty_u16(32768)
        time.sleep(duracion_beep)
        buzzer.duty_u16(0)
        time.sleep(pausa_entre)
    time.sleep(1)

