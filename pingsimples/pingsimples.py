#importando módulo de Operational System. OS integra os programas e recursos
#de um sistema operacional
import os
ip_ou_host = input("Digite o IP ou host destino: ") #Imprime a solicitacao de entrada de dados após criar a variável
os.system('ping -n 6 {}'.format(ip_ou_host)) #Formata os dados para a saída de console