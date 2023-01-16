# p2pLoraCommunication

Peer to peer communication between two RaspberryPi Picos and Grove LoRa e5 transmitters. I created this project to track wildlife.
The transmitter device is equipped with a motion sensor, and it is placed along a route that animals use.
The receiver device is at home, and it creates a webserver where the motion sensor data is logged. 
This way, I will be able to know when and where the animals are active which is useful when trying to photograph them.


PARTS NEEDED

- RaspberryPi Pico (transmitter)
- RaspberryPi Pico W (receiver)
- 2x Grove LoRa E5
- Battery pack for the transmitter, the receiver can be plugged into a socket
- Jumper wires

WIRING




CODE

Put the receivermain.py and transmittermain.py into the receiver and transmitter Picos and rename both of them main.py so they will run when powered up.
