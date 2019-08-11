import socket
import time
from gpiozero import LEDBoard
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.43.144", 5005))
s.listen(5)

oneA = LEDBoard(2, 3)
oneB = LEDBoard(4, 14)
twoA = LEDBoard(15, 18)
twoB = LEDBoard(17, 27)
# leds = [oneAleds, oneBleds, twoAleds, twoBleds]

BUFFER = 50
print("Server started ...")
while True:
    client, address = s.accept()
    print("Connection from {} has been established.".format(address))
    while True:
    msg = client.recv(BUFFER)
    msg = msg.decode()
    command, id = msg.split(";")
    if command == 'ON':
        print(command, id)
        if id == 'ONEA':
            oneA[1].on()
            oneA[0].off()
        if id == 'ONEB':
            oneB[1].on()
            oneB[0].off()
        if id == 'TWOA':
            twoA[1].on()
            twoA[0].off()
        if id == 'TWOB':
            twoB[1].on()
            twoB[0].off()
    if command == 'OFF':
        print(command, id)
        if id == 'ONEA':
            oneA[1].off()
            oneA[0].on()
        if id == 'ONEB':
            oneB[1].off()
            oneB[0].on()
        if id == 'TWOA':
            twoA[1].off()
            twoA[0].on()
        if id == 'TWOB':
            twoB[1].off()
            twoB[0].on()
    client.close()

