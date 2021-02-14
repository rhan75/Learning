import socket
#import threading

#HEADER = 10
msg = "Welcome to the server!"
#print(f'{len(msg):<10}')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 10000))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established!')
    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADER}}' + msg 
 
    clientsocket.send(bytes(msg, 'utf-8'))
    clientsocket.close()




'''
exit_signal = threading.Event()
HEADER = 64
PORT = 10000
SERVER = socket.gethostbyname(socket.gethostname()) 
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'disconnect!'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    try:
        print(f'[New Connection] {addr} connected')

        connected = True
        while connected:
            msg = conn.recv(HEADER).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f'[{addr}] {msg}')

        conn.close()
    except KeyboardInterrupt:
        print('Connection closed')
        conn.close()



print("[STARTING] Server is starting....")
server.listen()
print(f'[LISTENING] Server is listening on {SERVER}')
running = True
try:
    while running:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[Active Connections] {threading.activeCount() -1}')
except KeyboardInterrupt:
    print('Thread successfully closed')
    running = False
'''