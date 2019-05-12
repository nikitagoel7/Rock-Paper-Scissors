import socketserver
from socket import *

port = 6000
host = ''

server = socket(AF_INET, SOCK_STREAM)
server.bind((host, port))

n = 0

server.listen(2)
print ("Ready for the game")

(con1, (c_ip1, c_host1)) = server.accept()

print ("Player 1 is found. Waiting for player 2")

(con2, (c_ip2, c_host2)) = server.accept()

print ("Player 2 arrived. Let's play")

def rock_paper_scissors(con1, con2, c_ip1, c_ip2, c_host1, c_host2):
    rounds = 1
    p1 = 0
    p2 = 0
    while rounds!= 4:
        message1 = "Round "+str(rounds)+ " Started!\n"
    
        print (message1)
        con1.send(message1.encode('utf-8'))
        con2.send(message1.encode('utf-8'))

        d1 = con1.recv(2048)
        m1 = d1.decode('utf-8')

        d2 = con2.recv(2048)
        m2 = d2.decode('utf-8')

        if m1 == m2:
            msg = '1 point recieved by both'
##            con1.send(msg.encode('utf-8'))
##            con2.send(msg.encode('utf-8'))
            p1 += 1
            p2 += 1
        elif (m1 == "Scissors" and m2 == 'Paper') or (m1 == "Rock" and m2 == "Scissors") or (m1 == "Paper" and m2 == "Rock"):
            msg = '1 point recieved by Player 1'
##            con1.send(msg.encode('utf-8'))
##            con2.send(msg.encode('utf-8'))
            p1 += 1
        else:
            msg = '1 point recieved by Player 2'
##            con1.send(msg.encode('utf-8'))
##            con2.send(msg.encode('utf-8'))
            p2 += 1
        print (msg)
        rounds += 1
    w = 'You Win'
    l = 'You Lose'
    if p1>p2:
        print("Player1 wins")
        con1.send(w.encode('utf-8'))
        con2.send(l.encode('utf-8'))
    elif p2>p1:
        print("Player2 wins")
        con1.send(l.encode('utf-8'))
        con2.send(w.encode('utf-8'))
    else:
        msg = "It is a tie"
        con1.send(msg.encode('utf-8'))
        con2.send(msg.encode('utf-8'))
        print (msg)
    
rock_paper_scissors(con1, con2, c_ip1, c_ip2, c_host1, c_host2)
