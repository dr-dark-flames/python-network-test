import socket
from _thread import *
import pickle
from player import *


server = "192.168.0.20"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
msg = "Welcome To The Server!"
print("Waiting for a connection")
print(f"{len(msg):<20}"+msg)


def read_pos(new_str):
    new_str = new_str.split(",")
    return int(new_str[0]), int(new_str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


players = [Player(0, 0, 50, 50, (255, 0, 0)),
           Player(100, 100, 50, 50, (0, 0, 255))]


def thread_client(c, player):
    c.send(pickle.dumps(players[player]))
    while True:
        try:
            data = pickle.loads(c.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Received: ", data)
                print("Sending : ", reply)

            c.sendall(pickle.dumps(reply))
        except socket.error and EOFError:
            break
    print("Lost connection")
    c.close()


current_player = 0
while True:
    connect, address = s.accept()
    print("Connected to: ", address)

    start_new_thread(thread_client, (connect, current_player))
    current_player += 1
