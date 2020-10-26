import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port1= 12345                #port number for face detection
port2= 12346                #port number for face recognition
port = int(input("Select a port number either 12345 or 12346: "))                           

s.connect((host, port))
print(s.recv(1024))
s.close()                     # Close the socket when done