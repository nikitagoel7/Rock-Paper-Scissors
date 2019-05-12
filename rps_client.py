from socket import *

host = gethostname()
port = 6000

client = socket(AF_INET, SOCK_STREAM)
client.connect((host, port))
rounds = 1
while 1:
    d = client.recv(2048)
    m = d.decode('utf-8')
    print (m)
    if rounds != 4:
##    d = client.recv(2048)
##    m = d.decode('utf-8')
        msg = input("Enter Scissors/ Rock/ Paper: ")        
        client.send(msg.encode('utf-8'))
    else:
        break
    rounds += 1
    
    
    
d = client.recv(2048)
m = d.decode('utf-8')
print (m)

