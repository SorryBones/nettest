import socket
import sys

HEADER = 2048
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = "x"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

def handle_client(conn, addr):
    msg_length = conn.recv(HEADER).decode(FORMAT) # Blocking line
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT) # Blocking line
        if msg == DISCONNECT_MSG:
            conn.close()
            print("Closing session, ending program...")
            sys.exit()
        print(f"[{addr}]: {msg}")

# Setting up server and connection to client
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print("Your local IP is: " + SERVER)
print("Waiting for connection...")
server.listen() # Blocking line
print(f"[LISTENING] Server is listening on {SERVER}")
conn, addr = server.accept()
print(f"[NEW CONNECTION] {addr} connected.")

# Messaging loop
for count in range(3):
    msg = input("Input message to send: ")
    if msg == DISCONNECT_MSG:
        conn.send(DISCONNECT_MSG.encode(FORMAT))
        conn.close()
        print("Closing session, ending program...")
        sys.exit()
    conn.send(msg.encode(FORMAT))
    print("Message sent!")
    print("Waiting to receive message...")
    handle_client(conn, addr)

print("\nSession over! Ending program.\n")
conn.close()
sys.exit()