from machine import Pin, PWM, I2C
import ssd1306
import uasyncio as asyncio
import urandom

# ---------------------------
# Configuración I2C y pantalla
# ---------------------------
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# ---------------------------
# Definición de botones (GPx)
# ---------------------------
gp2  = Pin(2, Pin.IN)
gp3  = Pin(3, Pin.IN)
gp6  = Pin(6, Pin.IN)
gp7  = Pin(7, Pin.IN)
gp20 = Pin(20, Pin.IN)

# ---------------------------
# Definición de switches (GPx)
# ---------------------------
gp8  = Pin(8, Pin.IN)
gp26 = Pin(26, Pin.IN)

# ---------------------------
# Buzzers
# ---------------------------
buzzer1 = PWM(Pin(21))
buzzer2 = PWM(Pin(27))
duty = 32768

melodia1 = [262, 294, 330, 349]   # DO-RE-MI-FA
melodia2 = [392, 440, 494, 523]   # SOL-LA-SI-DO

duracion = 0.2
pausa = 0.05

async def reproducir(buzzer, notas, duracion, pausa, repeticiones):
    for _ in range(repeticiones):
        for freq in notas:
            buzzer.freq(freq)
            buzzer.duty_u16(duty)
            await asyncio.sleep(duracion)
            buzzer.duty_u16(0)
            await asyncio.sleep(pausa)
    buzzer.duty_u16(0)  # apagar al final

# ---------------------------
# LEDs aleatorios
# ---------------------------
led_pins = [9, 10, 11, 12, 13, 14, 15]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

async def leds_random(duracion_total):
    tiempo = 0
    while tiempo < duracion_total:
        for led in leds:
            led.value(0)
        led = urandom.choice(leds)
        led.value(1)
        await asyncio.sleep(0.05)
        tiempo += 0.05
    # apagar todos al final
    for led in leds:
        led.value(0)

# ---------------------------
# Mostrar título BlackBox
# ---------------------------
async def mostrar_titulo(duracion_total):
    tiempo = 0
    while tiempo < duracion_total:
        oled.fill(0)
        oled.text(" BlackBox ", 30, 12)
        oled.show()
        await asyncio.sleep(0.2)
        tiempo += 0.2

# ---------------------------
# Mostrar botones/switches
# ---------------------------
async def mostrar_oled():
    while True:
        oled.fill(0)
        oled.text("2:{} 3:{} 6:{}".format(gp2.value(), gp3.value(), gp6.value()), 0, 0)
        oled.text("7:{} 20:{}".format(gp7.value(), gp20.value()), 0, 10)
        oled.text("8:{} 26:{}".format(gp8.value(), gp26.value()), 0, 20)
        oled.show()
        await asyncio.sleep(0.2)

# ---------------------------
# Programa principal
# ---------------------------
async def main():
    # 1) Intro: melodías 3 veces + LEDs + título
    await asyncio.gather(
        reproducir(buzzer1, melodia1, duracion, pausa, 3),
        reproducir(buzzer2, melodia2, duracion, pausa, 3),
        leds_random( len(melodia1)* (duracion+pausa) * 3 ),  # duración aproximada
        mostrar_titulo( len(melodia1)* (duracion+pausa) * 3 )
    )

    # 2) Modo normal: solo pantalla con botones/switches
    await mostrar_oled()

asyncio.run(main())
