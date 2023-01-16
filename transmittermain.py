import time
from machine import UART, Pin

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)
pir = Pin(16, Pin.IN, Pin.PULL_DOWN)

uart.write('AT+MODE=TEST\r\n')
msg = 'AT+TEST=TXLRPKT "ABCD"\r\n'

while True:
     if pir.value() == 1:
        uart.write(msg)
        time.sleep(1)
        print(uart.read())
        time.sleep(30)
