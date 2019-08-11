import socket
import time
from gpiozero import LEDBoard
oneA = LEDBoard(2, 3)
oneB = LEDBoard(4, 14)
twoA = LEDBoard(15, 18)
twoB = LEDBoard(17, 27)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("192.168.43.144", 5005))
    s.listen(5)
    print("Server started ...")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(50)
            if not data:
                break
            data = data.decode()
            command, id = data.split(";")
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
