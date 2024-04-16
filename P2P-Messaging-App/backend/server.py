import socket
import threading

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            conn.sendall(data)  # Echo back the received message (optional)
    finally:
        conn.close()

def create_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")

    try:
        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
    finally:
        server_socket.close()

if __name__ == "__main__":
    HOST = '127.0.0.1'  # Localhost
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
    create_server(HOST, PORT)
