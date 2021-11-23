import socket
import requests

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

host = socket.gethostname()
port = 5555
soc.bind((host, port))
soc.listen(5)

headers = {
    'Accept': 'text/plain',
}

response = requests.get("https://icanhazdadjoke.com/", headers=headers)
joke = response.text

while True:
    cl, addr = soc.accept()
    print('Have connection from ', addr)
    cl.send(joke.encode())
    handshake = cl.recv(1024).decode()
    print(handshake)
    outfile = open('client_handshake.txt','a')
    outfile.write(handshake + "\n")
    f = open("client_handshake.txt", "r")
    print("View older handshakes : ")
    print(f.read())
    break
print("Closing connection")
cl.close()
