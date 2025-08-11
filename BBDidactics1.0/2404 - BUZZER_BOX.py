#6. Sonidos c. Uso del Buzzer
from machine import Pin, PWM
import time

buzzer = PWM(Pin(2))

secuencia = [2000, 2500, 3000, 3500]
duracion_beep = 0.05
pausa_entre = 0.02

while True:
    for freq in secuencia:
        buzzer.freq(freq)
        buzzer.duty(512)
        time.sleep(duracion_beep)
        buzzer.duty(0)
        time.sleep(pausa_entre)
    time.sleep(1)
