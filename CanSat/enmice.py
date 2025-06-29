from machine import Timer, Pin, I2C
import machine, dht, time
from BME280 import BME280
import uos  # necesario para verificar tamaño del archivo

# pin
d = dht.DHT11(machine.Pin(28))
tim1 = Timer()
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=100000)
bme = BME280(i2c=i2c)

def get_tiempo():
    t = time.localtime()
    return f"{t[3]:02}:{t[4]:02}:{t[5]:02}"

def guardar_archivo(nombre_archivo, fila):
    ruta = f"/{nombre_archivo}.csv"
    encabezado = "Tiempo,Temp_DHT,Humedad_DHT,Temp_BME,Presion_BME"
    try:
        try:
            stat = uos.stat(ruta)
            archivo_vacio = stat[6] == 0
        except OSError:
            archivo_vacio = True

        with open(ruta, "a") as archivo:
            if archivo_vacio:
                archivo.write(encabezado + "\n")
            archivo.write(fila + "\n")
    except Exception as e:
        print("Error al guardar: ", e)

def CanSat(timer):
    # dht
    d.measure()
    temp1 = d.temperature()
    hmd1 = d.humidity()
    # bme
    temp2 = bme.temperature
    pres = bme.pressure
    # hora
    tiempo = get_tiempo()
    filacsv = f"{tiempo},{temp1},{hmd1},{temp2},{pres}"
    guardar_archivo("2906 - Pruebas ENMICE 2", filacsv)
    print("Dato guardado: ", filacsv)

tim1.init(period=1000, mode=Timer.PERIODIC, callback=CanSat)

