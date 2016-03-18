import socket
import atexit

import core
import parser

from config import *

def process(conn, addr):
    print("(info) Wait for game data...")
    buf = conn.recv(BUFFER_SIZE)

    print("(info) Parsing data...")
    data = parser.parse_data(buf)

    print("(info) Computing...")
    solver = core.Solver(data)
    x, y = solver.compute()

    print("(info) Sending back...")
    message = "{}{}".format(chr(x), chr(y))
    conn.send(message.encode("ascii"))

def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(MAX_CONNECTIONS)
    atexit.register(sock.close)

    while True:
        conn, addr = sock.accept()
        print("(info) New connection from {}:{}".format(
            addr[0], addr[1]
        ))

        process(conn, addr)

        conn.close()
        print("(info) Close connection from {}:{}".format(
            addr[0], addr[1]        
        ))
