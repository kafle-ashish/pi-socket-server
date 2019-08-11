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
    msg = client.recv(BUFFER)
    msg = msg.decode()
    command, id = msg.split(";")
    # if command == 'ON':
    print(command, id)
    #     if msg[2:6] == 'onea':
    #         oneA[0].on()
    #         oneA[1].off()
    # if msg[:3] == 'OFF':
    #     print(msg[:3], "changing to off")
    #     oneA[0].off()
    #     oneA[1].on()
    

