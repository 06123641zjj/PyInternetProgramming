import sys,socket

port=70
host="quux.org"

fileName=b'/'

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))
#注意 此处要转码为b 因为缓存设为0了
fd=s.makefile('rwb',0)

fd.write(fileName+b'\r\n')

for line in fd.readlines():
    sys.stdout.write(line.decode('UTF-8'))

