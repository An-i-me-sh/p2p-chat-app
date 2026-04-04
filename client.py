import socket
import threading 

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    # print(client.recv(2048).decode(FORMAT))

def receive():
    while True:
        try:
            msg_length = client.recv(HEADER)
            
            if not msg_length:
                break
            
            msg_length = int(msg_length.decode(FORMAT))
            msg = client.recv(msg_length).decode(FORMAT)
            print(f"\n{msg}")
            print("You: ", end="", flush=True)
            

        except:
            print("[ERROR] Connection closed")
            break

thread = threading.Thread(target=receive)
thread.start()

username = input("Enter you name:")
send(username)


while True:
    msg = input("You:")

    if msg.lower() == "disconnect":
        send(DISCONNECT_MESSAGE)
        break
    
    
    send(msg)
    
