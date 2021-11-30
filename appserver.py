import socket
import threading

receiverip = "0.0.0.0"
receiverport = 4642
#st = "<sep>"
client_socket = set()

#Server Socket
server = socket.socket()
print("Socket created")
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind( (receiverip, receiverport) )
print("Socket binded")
server.listen(5)
print(f"Socket listening as {receiverip}:{receiverport}")


def listen(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"[!] Error: {e}")
            client_socket.remove(cs)
        for client in client_socket:
            client.send(msg.encode())
            print(f"msg sent {addr}")



while True:
    client, addr = server.accept()
    print(f"Connection accepted from {addr}")
    client_socket.add(client)
    print("Client Added")
    receivt = threading.Thread(target=listen, args=(client, ))
    receivt.daemon = True
    receivt.start()


for cs in client_socket:
        cs.close()

server.close()
        





    