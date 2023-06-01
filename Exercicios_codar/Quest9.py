import socket

def getDns(ip):
    try:
        host = socket.gethostbyaddr(ip)[0]
        return host
    except socket.herror:
        return "Unknown"
    
l= int(input())
ips =[]

for i in range(l):
    ips.append(input())

for ip in ips:
    print(getDns(ip))

1