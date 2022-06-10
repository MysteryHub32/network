import socket

server_ip='127.0.0.1'
port = 9999

server = socket.socket()

server.bind((server_ip, port))
server.listen(1)
print('====Server is ready====')

client, adder = server.accept()
print('====Client has connected====')

msg = client.recv(1024)
print('====Message Received====')

client.send(b'Hi Hi I\'m server. You\'re name is: ' + msg)
print('====Message Sent====')

client.close()
server.close()