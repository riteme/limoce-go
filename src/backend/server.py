import socket

from config import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(MAX_CONNECTIONS)

def process(conn, addr):
    pass

while true:
    conn, addr = sock.accept()
    print("(info) New connection from {}:{}".fromat(
        addr[0], addr[1]
    ))

    process(conn, addr)

    conn.close()
    print("(info) Close connection from {}:{}".fromat(
        addr[0], addr[1]        
    ))
