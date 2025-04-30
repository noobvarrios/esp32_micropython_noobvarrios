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
    
def http_get(url):
    import socket
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()

do_connect()
valor = 147
dato_blackbox = "https://noobbarrrios.pythonanywhere.com/blackbox?dato={}".format(valor)
http_get(dato_blackbox)


"""
#emmanuelbarrios 30abril2025
from flask import Flask, request
#import json
#import time

app = Flask(__name__)

@app.route('/')
def principal():
    html = open('mysite_barrios/templates/principal.html','r')
    paginaprincipal = html.read()
    html.close()
    return paginaprincipal

@app.route('/blackbox') #/blackbox?dato=123
def blackbox():
    dato= str(request.args.get('dato'))
    f=open("mysite_barrios/blackbox.txt","w+")
    f.write(dato)
    f.close()
    return "Dato recibido por BlackBox."

@app.route('/show_blackbox')
def show_blackbox():
    f = open("mysite_barrios/blackbox.txt","r")
    x = f.read()
    f.close()
    p = open("mysite_barrios/templates/main_blackbox.html","r")
    pag = p.read()
    p.close()
    return pag.format(x)
"""
