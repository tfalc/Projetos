# O falczy tem um computador compartilhado e deseja que seus arquivos sejam criptografados para que ninguém tenha acesso
# a esses arquivos.
#
# A criptografia maluca do falczy define que:
#     - As letras dos arquivos devem ser trocadas por números conforme correspondência. Ex.: a=1, b=2, c=3 ... z=26.
#     - Após transformar uma letra em número, deve ser inserido um _ após esse número.
#     - A extensão do arquivo deve ser alterada para .falczy
#
# O arquivo deve ter somente letras minúsculas!
#
# Exemplos de saída:
# +-------------+-------------------------+
# |   Entrada   |          Saída          |
# +-------------+-------------------------+
# | gabi.txt    | 7_1_2_9.falczy          |
# | prova.txt   | 16_15_18_22_1.falczy    |
# | segredo.txt | 19_5_7_18_5_4_15.falczy |
# +-------------+-------------------------+

# Atribuição de letra para números:
letras = list(map(chr, range(ord('a'), ord('z') + 1)))
numeros = list(range(1, len(letras) + 1))
dicionario = dict(zip(letras, numeros))

fileName = input("Digite o nome do arquivo de texto com a extensão .txt: ")
print("Você inseriu o nome de arquivo: ", fileName)

# Testa se extensão é .txt
if fileName[len(fileName)-4:len(fileName)].lower() != '.txt':
    print("Extensão de arquivo inválida. Esta criptografia aceita somente arquivos .txt!")
    exit()

# Converte o arquivo para minúsculas
if fileName != fileName.lower():
    fileName = fileName.lower()
    print("Nome contém letras maiúsculas. O nome convertido para minúsculas é: ", fileName)

# Removendo a extensão do aquivo:
fileNameWithoutExtension = fileName.replace(".txt", "")

if fileNameWithoutExtension.isalpha():
    print("Convertendo o nome do arquivo...")
    print("-" * 60)
else:
    print("Nome do arquivo não pode conter números. Repita a operação.")
    exit()

# Convertendo o nome do arquivo em números
fileNameWithoutExtensionCryp = [str(dicionario[letra]) for letra in fileNameWithoutExtension]

# Realizando a alteração do arquivo
print("_".join(fileNameWithoutExtensionCryp) + ".falczy")
print("-" * 60)