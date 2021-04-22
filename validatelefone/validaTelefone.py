import phonenumbers
from phonenumbers import geocoder


telefone = input("Digite o telefone: ")

telefone_num = phonenumbers.parse(telefone)

print(geocoder.description_for_number(telefone_num, 'pt'))