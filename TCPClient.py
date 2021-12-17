from socket import *

serverName = 'localhost'
serverPort = 12001

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input('Input lowercase sentence: ')
clientSocket.send(bytes(sentence, 'UTF-8'))

modifiedSentence =  clientSocket.recv(1024)
print(f'From server: {modifiedSentence}')

clientSocket.close()