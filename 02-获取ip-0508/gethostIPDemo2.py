import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
# ip = socket.gethostbyname_ex(hostname)

print (ip)
