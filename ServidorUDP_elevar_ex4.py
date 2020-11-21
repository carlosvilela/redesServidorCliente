#!/usr/bin/python3

# importando bibliotecas
import socket

# Variaveis
hostname = "localhost"                                                          # endereço local
porta = 1404                                                                    # porta de comunicação
tamanhoBuffer = 4*(1024)                                                        # Tamanho do Buffer

# Criando Sockets UDP
codeServidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                 # Cria Socket UDP
codeServidor.bind((hostname, porta))                                            # hostname e porta de acesso

# Função para calcular o valor elevando a constante neperiana
def elevar (valor):
    potencia = 2,7182818284590452353602874
    calculo = math.pow(valor,potencia)
    return calculo

# Loop infinito, aguardando requisições
try:                                                                        # tratamento de erros
    while True:
        mensagem,endCliente = codeServidor.recvfrom(tamanhoBuffer)          # recebe a mensagem do Cliente
        mensagem = mensagem.decode("ascii")                                 # converte os bytes na tabela ascii
        valor = float(mensagem)                                             # converte a string em numero inteiro
        calc = elevar(valor)                                            # realiza os calculos
        mensagem = str(calc).encode("utf-8")                                # converte o numero inteiro em string
        codeServidor.sendto(mensagem,endCliente)                            # retorna a mensagem processada ao cliente

except KeyboardInterrupt:                                                   # caso haja erro irá retornar uma ação
    codeServidor.close()