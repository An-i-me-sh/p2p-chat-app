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

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                for client in clients:
                    if client != conn:
                        client.send(msg.encode(FORMAT))
                        
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                print(f"[{addr}] {msg}")
                # conn.send("Msg received".encode(FORMAT))
        except:
            print(f"[DISCONNECTED] {addr} connection lost")
            break


    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        clients.append(conn)

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting..")
start()