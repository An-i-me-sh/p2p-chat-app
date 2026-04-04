import socket
import threading

HEADER = 64
PORT = 5050

SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
#print(socket.gethostname())

ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []
usernames = {}

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    #for storing user name 
    msg_length = conn.recv(HEADER)
    msg_length = int(msg_length.decode(FORMAT))
    username = conn.recv(msg_length).decode(FORMAT)
    usernames[conn] = username

    print(f"[USERNAME] {addr} is {username}")

    connected = True
    while connected:
        try:
            msg_length = conn.recv(HEADER)

            if not msg_length:
                break

            msg_length = int(msg_length.decode(FORMAT))   
            msg_data = conn.recv(msg_length)

            if not msg_data:
                break

            msg = msg_data.decode(FORMAT)
            print(f"[{addr}] {msg}")

            if msg == DISCONNECT_MESSAGE:
                break

            print(f"[DEBUG] Total clients: {len(clients)}")

            for client in clients:
                if client.fileno() != conn.fileno():
                    try:
                        print(f"[BROADCAST] sending to {client}")
                        send_msg(client, f"{usernames[conn]}: {msg}")
                    except Exception as e:
                        print(f"[ERROR SENDING] {e}")
                        if client in clients:
                            clients.remove(client)
                        
            
        except Exception as e:
            print(f"[ERROR] {addr} as e")
            break
        
    if conn in clients:
        clients.remove(conn)

    if conn in usernames:
        del usernames[conn]

    conn.close()
    print(f"[DISCONNECTED] {addr}")
                    
    

def send_msg(conn, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    conn.send(send_length)
    conn.send(message)

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        print(f"[CLIENTS] {len(clients)} connnected")

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting..")
start()