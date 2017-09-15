import socket,sys

port=70
host='quux.org'

filename=b'/'

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect((host,port))
except socket.gaierror as e:
    print('Error connecting to server %s' % e)
    sys.exit(1)
s.sendall(filename+b'\r\n')

while True:
    buf=s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf.decode('UTF-8'))