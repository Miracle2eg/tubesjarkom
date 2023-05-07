import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8080

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock_server.bind((SERVER_HOST, SERVER_PORT))

sock_server.listen()

print("Server ready....")

while True:
    sock_client, client_address = sock_server.accept()

    request = sock_client.recv(1024).decode()
    print("Dari Client :"+request)

    response = "Ini dari server :"+request
    sock_client.send(response.encode())

    sock_client.close()
#endwhile
sock_server.close()
    
