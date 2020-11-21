#!/usr/bin/python3

# importando bibliotecas
import socket

# Variaveis
hostname = "localhost"                                                          # endereço local
porta = 1404                                                                    # porta de comunicação
tamanhoBuffer = 4*(1024)                                                        # Tamanho do Buffer

# Criando Sockets UDP
codeCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                  # Cria Socket UDP

enviar = input("Digite um valor: ")                                             # entrada de dados
codeCliente.sendto(enviar.encode(),(hostname,porta))                            # envio da mensagem
resultado,endServidor = codeCliente.recvfrom(1048)                              # recebe a resposta do servidor
resultado = (resultado).decode()                                                # Decodificar resultado

print("extraindo 25% de ",enviar," perfaz o valor de ",resultado)               # exibe a resposta do servidor

codeCliente.close()                                                             # finaliza a conexão