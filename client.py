import socket
UDP_IP_ADDRESS="127.0.0.1"
UDP_PORT_NO=6788
Message=("hello friend")
bytesTosend=str.encode(Message)
clientsock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientsock.sendto(bytesTosend,(UDP_IP_ADDRESS,UDP_PORT_NO))
