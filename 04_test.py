from socket import *

s = socket()

s.bind(("127.0.0.1",8888))
s.listen(5)
while True:
    c, addr = s.accept()
    data = c.recv(1024)
    s.send("好捞哦")
c.close()
s.close()
