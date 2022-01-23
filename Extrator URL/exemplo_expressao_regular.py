endereco = "Rua Renato de Lacerda, 59 - Casa A, Vila Sabrina, São Paulo - SP - 02138-060"

import re # Regular Expression -- RegEx

#Cep contém: 5 digitos + hifén (opicional) + 3 digitos

padrão = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrão.search(endereco) #retorn tipo Match
print(type(busca))
if busca:
    cep = busca.group()
    print(cep)