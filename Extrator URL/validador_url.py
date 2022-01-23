'''
Exemplos de URLs válidas:
    bytebank.com/cambio
    bytebank.com.br/cambio
    www.bytebank.com/cambio
    www.bytebank.com.br/cambio
    http://www.bytebank.com/cambio
    http://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio


Exemplos de URLs inválidas:
    https://bytebank/cambio
    https://bytebank.naoexiste/cambio
    ht://bytebank.naoexiste/cambio
'''

import re

test_url = 'bytebank.com.br/cambio'

default_url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = default_url_pattern.match(test_url)

if not match:
    raise ValueError("A URL NÃO é válida")

print("A URl é Valida!")