import http.client

L = int(input())
dom = []

for i in range(L):
    dom.append(input())

def HTTPclient(host,port):
    conn = http.client.HTTPConnection(host,port)

    for dominio in dom:
        conn.request("GET",dom)

        r1 = conn.getresponse()

        data1 = r1.getheaders('dom-Type')

        if data1 == "audio/mpeg":
            print("Playing audio:", dom)
        elif data1 == "text/html":
            print("Browsing:", dom)
        elif data1 == "video/x-msvideo":
            print("Playing media:", dom)
        elif data1 == "application/json":
            print("Processing JSON:", dom)
        elif data1:
            print("Unknown file/media:", data1, "-", dom)
        else:
            print("Content not found")