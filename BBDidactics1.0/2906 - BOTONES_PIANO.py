#3. Lectura de Botones b. Eventos a partir de combinacion de botones.
#6. Sonidos. b. Escalas Musicales. 
from machine import Pin, PWM, Timer
import time

# Configurar botones
btn1 = Pin(35, Pin.IN, Pin.PULL_UP)
btn2 = Pin(34, Pin.IN, Pin.PULL_UP)
btn3 = Pin(39, Pin.IN, Pin.PULL_UP)
btn4 = Pin(36, Pin.IN, Pin.PULL_UP)

# Configurar buzzer
buzzer = PWM(Pin(2))
buzzer.duty(0)  # Empieza en silencio

# Diccionario de notas (frecuencia en Hz)
notas = {
    "DO": 261,
    "RE": 294,
    "MI": 329,
    "FA": 349
}

# Función que revisa los botones y toca la nota correspondiente
def tocar_piano(timer):
    if btn1.value() == 0:  # Botón presionado (activo en bajo)
        buzzer.freq(notas["DO"])
        buzzer.duty(512)
    elif btn2.value() == 0:
        buzzer.freq(notas["RE"])
        buzzer.duty(512)
    elif btn3.value() == 0:
        buzzer.freq(notas["MI"])
        buzzer.duty(512)
    elif btn4.value() == 0:
        buzzer.freq(notas["FA"])
        buzzer.duty(512)
    else:
        buzzer.duty(0)  # Silencio si no hay botones presionados

# Usar timer para revisar constantemente
tim = Timer(1)
tim.init(period=50, mode=Timer.PERIODIC, callback=tocar_piano)
