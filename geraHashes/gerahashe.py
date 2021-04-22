import hashlib

umaString = input("Digite a palavra ou o texto que deseja gerar um hash: ")
menu = int(input(''' #### MENU - ESCOLHA O TIPO DE HASH #### 
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o número do has que deseja gerar: '''))

if menu == 1:
    hashgerado = hashlib.md5(umaString.encode('utf-8'))
    print("A hash em MD5 da entrada (", umaString, ") é: ", hashgerado.hexdigest())
elif menu == 2:
    hashgerado = hashlib.sha1(umaString.encode('utf-8'))
    print("A hash em SHA1 da entrada (", umaString, ") é: ", hashgerado.hexdigest())
elif menu == 3:
    hashgerado = hashlib.sha256(umaString.encode('utf-8'))
    print("A hash em sha256 da entrada (", umaString, ") é: ", hashgerado.hexdigest())
elif menu == 4:
    hashgerado = hashlib.sha512(umaString.encode('utf-8'))
    print("A hash em sha512 da entrada (", umaString, ") é: ", hashgerado.hexdigest())
else:
    print("Opção inválida!")

#usar b'' para converter string em bytes
resultado = hashlib.md5(b'Python Security')
string = input("Digite sua senha para gerar o hash: ")
convertString = hashlib.md5(string.encode('utf-8'))

print("-" * 40)
print("O hash da string Python Security em md5 é: ", resultado.hexdigest())
print("O hash da sua senha digitada (", string,  ") em md5 é: ", convertString.hexdigest())