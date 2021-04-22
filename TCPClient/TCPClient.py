import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Não foi possível realizar a conexão")
        print("Falha: {}".format(e))
        sys.exit()
    print("Socket criado com sucesso!")

    hostAlvo = input("Digite o IP/host desejo: ")
    portaAlvo = input("Digite a porta que deseja fazer conexão: ")

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print("Conexão realizada com sucesso!")
        print("Conectado com o host: " + hostAlvo + " e com a porta: " + portaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("A conexão com o host " + hostAlvo + ":" + portaAlvo + " falhou.")
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()