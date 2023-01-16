import network
import socket
import time
from machine import Pin, I2C, UART
import sys
import machine
import struct

led = machine.Pin("LED", machine.Pin.OUT)
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)
uart.write('AT+MODE=TEST\r\n')
lastSeen = ""
juu = True
time.sleep(5)
ssid = '***********' #Your network name
password = '*********' #Your WiFi password
NTP_DELTA = 2208988800
host = "pool.ntp.org"

#initialize I2C 
i2c= machine.ADC(4)
conversion_factor = 3.3 / (65535)

def set_time():
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = socket.getaddrinfo(host, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.settimeout(1)
        res = s.sendto(NTP_QUERY, addr)
        msg = s.recv(48)
    except OSError as exc:
        if exc.args[0] == 110:
            time.sleep(2)
            pass
    finally:
        s.close()
    val = struct.unpack("!I", msg[40:44])[0]
    t = val - NTP_DELTA    
    tm = time.gmtime(t)
    machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

max_wait = 10

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage(reading):
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>Pico W Weather Station</title>
            <meta http-equiv="refresh" content="10">
            </head>
            <body>
            <p>{reading}</p>
            </body>
            </html>
            """
    return str(html)
    
def serve(connection):
    #Start a web server
    uart.write('AT+TEST=RXLRPKT\r\n')
    time.sleep(1)
    lastSeen = str(time.localtime(3))
    while True:
        readingki = i2c.read_u16() * conversion_factor
        temperature = 27 - (readingki - 0.706)/0.001721 
        reading = "Temperature: {}".format(temperature) + " / Viimeksi nähty " + lastSeen
        byte_read = uart.readline()
        if byte_read != None:
            if "ABCD" in byte_read:
                print("joodjdj")
                lastSeen = str(time.localtime())
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)       
        html = webpage(reading)
        client.send(html)
        client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    set_time()
    print(time.localtime())
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
