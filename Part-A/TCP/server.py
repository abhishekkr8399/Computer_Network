import socket, os
HOST = "localhost" # The server's hostname or IP address
PORT = 5000 # The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
 s.bind((HOST, PORT))
 s.listen(1)
 while True:
    print('\nWaiting for client connection...')
    conn, addr = s.accept()
    with conn:
        print("Connection from:", addr)
        while True:
            filename = conn.recv(1024).decode()
            if not filename:
                break
            print('Requested filename:', filename)
            if not os.path.exists(filename):
                print('Status: File not found.')
                conn.sendall(b'file not found')
            else:
                with open(filename) as file:
                    conn.sendall(file.read().encode())
                print('Status: File transmitted...')
                break
        print("Closing this connection...")