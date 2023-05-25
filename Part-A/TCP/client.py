import socket
HOST = "127.0.0.1" # The server's hostname or IP address
PORT = 5000 # The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
 filename = input('Enter the filename: ')
 s.connect((HOST, PORT))
 print('Connected to ', HOST)
 s.sendall(filename.encode())
 print('Filename sent...')
 data = s.recv(1024).decode()
 if data.startswith('file not found'):
    print(f'Requested file {filename!r} not found in server {HOST!r}.')
 else:
    print(f'Receiving requested file {filename!r}...', end='')
    with open("d"+filename, 'w') as file:
        while True:
            file.write(data)
            if not data: break
            data = s.recv(1024).decode()
    print('done.')
 s.close()