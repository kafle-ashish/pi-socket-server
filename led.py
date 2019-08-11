from sock import Sock

conn = Sock(ip="192.168.43.144")
conn.connect()
conn.send("ON;ONEB")