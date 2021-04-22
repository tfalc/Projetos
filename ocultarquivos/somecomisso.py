import ctypes

atributo_ocultar = 0x02
arquivo = 'ocultar.txt'

retorno = ctypes.windll.kernel32.SetFileAttributesW(arquivo, atributo_ocultar)

if retorno:
    print("Arquivo foi ocultado")
else:
    print("Arquivo não encontrado ou não foi possível ocultar o arquivo")