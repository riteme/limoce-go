import sys
import imp
import copy
import socket
import atexit
import threading
# import readline
import traceback

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
    message = "{}{}".format(chr(y), chr(x))
    conn.send(message.encode("ascii"))

def _run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(MAX_CONNECTIONS)

    try:
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
    finally:
        sock.close()

def run():
    t = threading.Thread(
        target=_run
    )
    t.deamon = True
    t.start()

    while True:
        command = raw_input(">>> ")
        print(command)
        command = command.strip().lower()

        if command == "reload":
            try:
                imp.reload(core)
            except Exception as e:
                print("(error) Can't reload core modules: {}".format(str(e)))

        elif command == "exit":
            sys.exit()

        else:
            print("(error) Unknown command: {}".format(command))
