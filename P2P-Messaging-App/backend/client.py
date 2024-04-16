import socket

def create_client(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    
    # User input for name and chatroom selection
    username = input("Enter your name: ")
    chatroom = input("Choose a chatroom (1, 2, or 3): ")
    while chatroom not in ['1', '2', '3']:
        print("Invalid chatroom. Please choose 1, 2, or 3.")
        chatroom = input("Choose a chatroom (1, 2, or 3): ")
    
    try:
        while True:
            message = input(f"{username} (Chatroom {chatroom}): ")
            full_message = f"{username} in Chatroom {chatroom}: {message}"
            client_socket.sendall(full_message.encode())
            data = client_socket.recv(1024)
            print(f"Received: {data.decode()}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 65432
    create_client(SERVER_HOST, SERVER_PORT)
