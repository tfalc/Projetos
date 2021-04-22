import itertools

string = input("String a ser permutada: ")

# permutação das palavras e caracteres no wordlist
# entrar com os caracteres e quer testar e a quantidade de testes
# O limite de testes é a quantidade de caracteres, portanto se usar 4, não será feito um teste
# É possível fazer testes com menos caracteres. O número define a quantidade de caracteres do teste
resultado = itertools.permutations('abc', 3)
for i in resultado:
    print(''.join(i))

#testando com palavra do input
resultado2 = itertools.permutations(string, len(string))
for i in resultado2:
    print(''.join(i))
