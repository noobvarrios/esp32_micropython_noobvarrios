import network
import urequests
import ujson
def do_connect():
    ssid = "varriendi"
    password = "12345678"
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    elif wlan.isconnected():
        print("Alredy Connected...")
    print('network config:', wlan.ifconfig())

do_connect()

response = urequests.get('https://worldtimeapi.org/api/timezone/America/Mexico_City')
json_data = ujson.loads(response.text)
print("JSON:", json_data)  # Para depuración
print(response)

