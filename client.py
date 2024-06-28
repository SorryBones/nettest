import socket
import sys

HEADER = 2048
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length)) # necessary length minus message length to get padding amount
    client.send(send_length) # padding sent throuugh socket
    client.send(message) # message sent through socket
    
# Input
SERVER = input("Enter the host's local IP: ") # SURROUND WITH TRY-EXCEPT IF IT FAILS TO CONNECT
ADDR = (SERVER, PORT)

# Connecting socket to host
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Messaging loop
for count in range(3):
    print("Waiting to receive message...")
    msg = client.recv(64).decode(FORMAT)
    if msg == DISCONNECT_MSG:
        print("Host quit. Ending program...")
        sys.exit()
    print(f"[{SERVER}]: {msg}")
    msg = input("Input message to send: ")
    if msg == DISCONNECT_MSG:
        print("Ending program...")
        sys.exit()
    send(msg)
    print("Message sent!")