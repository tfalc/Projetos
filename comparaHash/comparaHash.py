import hashlib

arquivoUm = 'testeUm.txt'
arquivoDois = 'testeDois.txt'

hash1 = hashlib.new('ripemd160')
hash2 = hashlib.new('ripemd160')

hash1.update(open(arquivoUm, 'rb').read())
hash2.update(open(arquivoDois, 'rb').read())

#digest resume os dados que são passados por um método update
if hash1.digest() != hash2.digest():
    print(f'O arquivo {arquivoUm} tem conteúdo diferente do arquivo {arquivoDois}')
    print(f'O hash do arquivo {arquivoUm} é: ' + hash1.hexdigest())
    print(f'O hash do arquivo {arquivoDois} é: ' + hash2.hexdigest())
else:
    print(f'O arquivo {arquivoUm} tem conteúdo semelhante do arquivo {arquivoDois}')


