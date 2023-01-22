# p2pLoraCommunication

Peer to peer communication between two RaspberryPi Picos and Grove LoRa e5 transmitters. I created this project to track wildlife.
The transmitter device is equipped with a motion sensor, and it is placed along a route that animals use.
The receiver device is at home, and it creates a webserver where the motion sensor data is logged. 
This way, I will be able to know when and where the animals are active which is useful when trying to photograph them.
 
 
This is what the graph on the website looks like:


![Näyttökuva 2023-01-21 231313](https://user-images.githubusercontent.com/84034458/213887383-e0ea34f6-e521-4115-b946-41f737e9c9c0.png)




The receiver on the left and the transmitter on the right, even Steve Jobs couldn't have done it better:


![IMG_20230122_142014](https://user-images.githubusercontent.com/84034458/213915765-6e2c2c0d-8d82-4804-9638-695ffdcd0338.jpg)



PARTS NEEDED

- RaspberryPi Pico (transmitter)
- RaspberryPi Pico W (receiver)
- 2x Grove LoRa E5
- Battery pack for the transmitter, the receiver can be plugged into a socket
- Jumper wires

WIRING


![transmitter](https://user-images.githubusercontent.com/84034458/213915950-5fd25cff-c7a0-476d-a0ce-4734130086b8.jpg)


The receiver is basically the same but without the battery and motion sensor.



CODE

Put the receivermain.py and transmittermain.py into the receiver and transmitter Picos and rename both of them main.py so they will run when powered up.


