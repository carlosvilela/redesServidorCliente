#!/usr/bin/python3

# importando bibliotecas
import socket

# Variaveis
hostname = "localhost"                                                          # endereço local
porta = 1404                                                                    # porta de comunicação
tamanhoBuffer = 4*(1024)                                                        # Tamanho do Buffer

# Criando Sockets TCP em IPv6
codeCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                 # Cria Socket TCP
codeCliente.connect((hostname, porta))                                          # Conexão com o Servidor

enviar = input("Digite um valor: ")                                             # entrada de dados
codeCliente.send(enviar.encode())                                               # envio da mensagem
resultado = codeCliente.recv(1048)                                              # recebe a resposta do servidor
resultado = (resultado).decode()                                                # Decodificar resultado
print("11% acrescido de ",enviar," é = ",resultado)                                 # exibe a resposta do servidor

codeCliente.close()                                                             # finaliza a conexão