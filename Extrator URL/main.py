url = 'https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'

print(url)

separator_index = url.find('?')

url_base = url[0:separator_index]
print(url_base)

url_parametros = url[separator_index+1:]
print(url_parametros)

search_parameter = 'moedaOrigem'
parameter_index = url_parametros.find(search_parameter)
print(parameter_index)
index_parameter_value = parameter_index + len(search_parameter) + 1
paremeter_value = url_parametros[index_parameter_value:]
print(paremeter_value)
