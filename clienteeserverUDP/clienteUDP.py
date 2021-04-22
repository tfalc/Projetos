import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente criado com sucesso!")

host = 'localhost'
porta = 5433
mensagem = 'Client to server message try \n'

try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente: ' + dados)
finally:
    print('Conexão está sendo encerrada')
    s.close()