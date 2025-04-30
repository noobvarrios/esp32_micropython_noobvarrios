#conexion con pythonanywhere. 
import machine, network, socket
s = socket.socket()

def do_connect():
    wlan = network.WLAN()
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('WiFi-DGAETIC', 'DGAnalisis-2024#')
        while not wlan.isconnected():
            machine.idle()
    print('network config:', wlan.ifconfig())
    
do_connect()


addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)
addr = addr_info[0][-1]
print(addr_info)
print(addr)

s.connect(addr)

while True:
    data = s.recv(500)
    print(str(data, 'utf8'), end='')