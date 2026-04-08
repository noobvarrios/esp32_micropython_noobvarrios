from machine import Pin, PWM, Timer
import time

sw1 = Pin(8, Pin.IN, Pin.PULL_DOWN)   
sw2 = Pin(26, Pin.IN, Pin.PULL_DOWN)  

buzzer_melodia = PWM(Pin(27))
buzzer_constante = PWM(Pin(22))

secuencia = [2000, 2500, 3000, 3500]
duracion_beep = 0.05
pausa_entre = 0.02

def switches(timer):
    if sw1.value() == 1:
        for freq in secuencia:
            buzzer_melodia.freq(freq)
            buzzer_melodia.duty_u16(32768) 
            time.sleep(duracion_beep)
            buzzer_melodia.duty_u16(0)
            time.sleep(pausa_entre)
    else:
        buzzer_melodia.duty_u16(0)  

    if sw2.value() == 1:
        buzzer_constante.freq(1000)    
        buzzer_constante.duty_u16(42768)   
    else:
        buzzer_constante.duty_u16(0)

tim1 = Timer()
tim1.init(period=500, mode=Timer.PERIODIC, callback=switches)
