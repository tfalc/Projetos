import ipaddress

ip = '192.168.0.100'
faixaIP = '192.168.0.0/30'
faixaIP2 = '192.168.0.50/24'


endereco = ipaddress.ip_address(ip)

# use strict=False para permitir entradas de faixas de IP com IPs definidos
rede = ipaddress.ip_network(faixaIP)
rede2 = ipaddress.ip_network(faixaIP2, strict=False)
print(endereco)
print(rede)
print(rede2)

print('\nA faixa de IP é: ' + faixaIP + ' e estes são os IPs disponíveis para ela: ')
for ip in rede:
    print(ip)