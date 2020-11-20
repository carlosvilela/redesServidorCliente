#!/usr/bin/python3

# importando bibliotecas
import socket

# Variaveis
hostname = "localhost"                                                          # endereço local
porta = 1404                                                                    # porta de comunicação
tamanhoBuffer = 4*(1024)                                                        # Tamanho do Buffer

# Criando Sockets TCP em IPv6
chatCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                 # Cria Socket TCP
chatCliente.connect((hostname, porta))                                          # Conexão com o Servidor

enviar = input("Digite um valor: ")                                             # entrada de dados
chatCliente.send(enviar.encode())                                               # envio da mensagem

resultado = chatCliente.recv(1048)                                              # recebe a resposta do servidor
print("O fatorial de ",enviar," é = ",resultado)                                 # exibe a resposta do servidor

chatCliente.close()                                                             # finaliza a conexão