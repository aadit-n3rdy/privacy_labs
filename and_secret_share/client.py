import socket
import random

isClient = False

conn = None
i = input("Connect to another client? ")
if i[0] in { 'y', 'Y' }:
    ip = input("Enter other client's IP address ")
    port = int(input("Enter port no. "))
    conn = socket.create_connection((ip, port))
    print(f"Connected to {ip}:{port}")
    isClient = True
else:
    port = int(input("Enter port no. "))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen()
    print(f"Listening on port {port}")
    conn, (ip, port) = sock.accept()
    print(f"Accepted conn from IP {ip}:{port}")

def genBitString(l: int):
    return random.randint(0, 2**l-1)

LAMBDA = 8
LBYTES = LAMBDA//8

x = random.getrandbits(LAMBDA)
y = random.getrandbits(LAMBDA)

print(f"x: {x}")
print(f"y: {y}")

# Following must be obtained from 3rd party
X = int(input("X? "))
Y = int(input("Y? "))
Z = int(input("Z? "))

otherX = 0
otherY = 0

if isClient:
    conn.send((x ^ X).to_bytes(LBYTES))
    conn.send((y^Y).to_bytes(LBYTES))

    otherX = int.from_bytes(conn.recv(LBYTES))
    otherY = int.from_bytes(conn.recv(LBYTES))
    z = (x & (y ^ otherY)) ^ Y & (otherX) ^ Z

    conn.send(z.to_bytes(LBYTES))
    otherZ = int.from_bytes(conn.recv(LBYTES))

    print(z ^ otherZ)

else:
    otherX = int.from_bytes(conn.recv(LBYTES))
    otherY = int.from_bytes(conn.recv(LBYTES))

    conn.send((x ^ X).to_bytes(LBYTES))
    conn.send((y^Y).to_bytes(LBYTES))

    z = (x & (y ^ otherY)) ^ Y & (otherX) ^ Z

    otherZ = int.from_bytes(conn.recv(LBYTES))
    conn.send(z.to_bytes(LBYTES))

    print(z ^ otherZ)

