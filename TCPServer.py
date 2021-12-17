from socket import * 

serverPort = 12001
serverName = 'localhost'

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    print(f'New messagem from {addr}: {sentence}')

    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)

    connectionSocket.close()