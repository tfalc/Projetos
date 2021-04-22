import os
import time

with open("hosts.txt") as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o destino ', ip)
        print('*' * 70)
        os.system('ping ' + ip)
        print('*' * 70)
        time.sleep(5)