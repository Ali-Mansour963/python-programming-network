import socket
import threading

f=open("d:\\f1.txt","r")
s = f.read()
qa = s.splitlines()
questions=[]
answers=[]
for i in range(0,20):
    questions.append(qa[i])
for j in range(20,40):
    answers.append(qa[j])

def handle_client(client_socket , client_address ):
    score = 0
    client_name = client_socket.recv(1024).decode()
    for i in range(len(questions)):
        client_socket.send(questions[i].encode())
        client_answer = client_socket.recv(1024).decode()
        if client_answer.lower() == answers[i].lower():
            client_socket.send(("اجابة صحيحة").encode())
            score += 1
        else:
            client_socket.send(("اجابة خاطئة").encode())
    print(client_name,score)
    score1 = str(score)
    client_socket.send((score1).encode())
    w = open("d:\\result.txt", "w")
    w.write('\n')
    w.write(client_name+score1)
    w.close()

server_socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 6666))
server_socket.listen(5)
print("Server started")

while True:
    client_socket, client_address = server_socket.accept()
    print("Client connected:", client_address)
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
