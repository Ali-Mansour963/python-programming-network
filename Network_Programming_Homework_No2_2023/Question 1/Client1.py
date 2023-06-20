import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 6666))
name_user = input('Enter your name:')
client_socket.send(name_user.encode())

while True:
    question = client_socket.recv(1024).decode()
    if not question:
        break
    answer = input(question)
    client_socket.send(answer.encode())

result = client_socket.recv(1024).decode()
print(result)

client_socket.close()
