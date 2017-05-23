import socket

host = "127.0.0.2"
port = 5000

s=socket.socket()
s.bind((host,port))

s.listen(1)
c,addr = s.accept()

print "connection from"+ str(addr)
while True:
	data = c.recv(1024)
	if not data:
		break
	print "from connectd user: "+str(data)
	data=str(data).upper()
	print "sending: "+str(data)
	c.send(data)
c.close()

