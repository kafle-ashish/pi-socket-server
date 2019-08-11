from sock import Sock

conn = Sock(ip="192.168.43.144")
while True:
    data = input("Enter the command please: \n")
    conn.connect()
    conn.send(data)
    conn.disconnect()
    print("Sent data: ", data)