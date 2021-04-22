import random
import string

tamanho = int(input('Digite o tamanho da senha que você quer criar: '))
chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+.:/?'
rnd = random.SystemRandom() #gera valores aleatórios a partir de fontes fornecidas pelo OS

# Para cada i no range tamanho, será gerado um valor aleatório até 16 (valor fixado na varíável) caracteres #
print('Sua senha é: ' + ''.join(rnd.choice(chars) for i in range(tamanho)))