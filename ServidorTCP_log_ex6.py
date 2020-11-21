#!/usr/bin/python3

# importando bibliotecas
import socket
import math

# Variaveis
hostname = "localhost"                                                          # endereço local
porta = 1404                                                                    # porta de comunicação
tamanhoBuffer = 4*(1024)                                                        # Tamanho do Buffer

# Criando Sockets TCP em IPv6
codeServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                # Cria Socket TCP
codeServidor.bind((hostname, porta))                                            # hostname e porta de acesso
codeServidor.listen(30)                                                         # numero de Conexões permitidas

# Função para calcular o logaritmo na base 10 de um valor
def logaritmo (valor):
    calculo = math.log10(valor)
    return calculo

# Loop infinito, aguardando requisições
try:                                                                        # tratamento de erros
    while True:
        clienteSocket, enderecoCliente = codeServidor.accept()              # Espera por conexão do cliente
        mensagem = clienteSocket.recv(tamanhoBuffer)                        # recebe a mensagem do Cliente
        mensagem = mensagem.decode("ascii")                                 # converte os bytes na tabela ascii
        valor = float(mensagem)                                             # converte a string em numero inteiro
        calc = logaritmo(valor)                                             # realiza os calculos
        mensagem = str(calc).encode("utf-8")                                # converte o numero inteiro em string
        clienteSocket.send(mensagem)                                        # retorna a mensagem processada ao cliente

except KeyboardInterrupt:                                                   # caso haja erro irá retornar uma ação
    codeServidor.close()