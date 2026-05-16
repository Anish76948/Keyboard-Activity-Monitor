# server.py
# Receives keyboard input from clients (for learning purposes)

import socket
import threading

HOST = "0.0.0.0"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server started... Waiting for connections")

def handle_client(conn, addr):
    print(f"Connected: {addr}")
    
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            
            text = data.decode()
            print(f"{addr}: {text}", end="")
        
        except:
            break

    conn.close()
    print(f"Disconnected: {addr}")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
