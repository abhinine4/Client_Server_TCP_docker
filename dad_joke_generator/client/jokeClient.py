import socket
import random

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

host = socket.gethostname()

port = 5555

soc.connect((host, port))
print("Connection established !")
jj = soc.recv(1024).decode()
print("View joke: ")
print(jj)

rn = random.randint(100, 1000)
tp = ("Thanks #client : " + str(rn))
print("Sending handshake: ")
soc.send(tp.encode())
soc.close()
