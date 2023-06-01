import http.client

def HTTPclient(host,port):
    conn = http.client.HTTPConnection(host,port)
    
    for dominio in dom:
        conn.request("GET", dominio)

        resposta = conn.getresponse()

        data = resposta.read().decode("utf-8")

        print(data)

    conn.close()



quantResquest = int(input())
dom =[]

for i in range(quantResquest):
    dom.append(input())

HTTPclient("aprednder3.unb.br",80)


