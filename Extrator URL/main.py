#URL Base para o estudo
url = 'https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'
print(url)
#------------------------------

#Utilizando a função find(...) encontrar o índice de um determinado carctere/palavra
#dentro de nossa string
separator_index = url.find('?')
#------------------------------

#Podemos utilzar uma funcionalidade nativa das strings para "fatiarmos" um pedaço  dela
#e salva-lo em uma nova variável

#Para isso basta utilizar nome_da_string[indice_inicial:indice_final]
#Lembre-se: indicie_inicial é inclusivo e indice_final é exclusivo
url_base = url[0:separator_index] 
print(url_base)
#------------------------------

#Podemos também não passar o segundo indice para pegarmos o restante da str 
url_parametros = url[separator_index+1:]
print(url_parametros)
#------------------------------

#Podemos passar um str intiera como parâmetro para a função find()
search_parameter = 'moedaOrigem'
parameter_index = url_parametros.find(search_parameter)
print(parameter_index) #Ela retornará o indice do INICIO da palavra encontrada na str
#------------------------------

#Com os valores em mãos, podemos usar de matemática básica para trazer o valor do
#atributo que queremos
index_parameter_value = parameter_index + len(search_parameter) + 1
paremeter_value = url_parametros[index_parameter_value:]
print(paremeter_value)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

search_parameter = 'moedaOrigem'
parameter_index = url_parametros.find(search_parameter)
print(parameter_index) 


index_parameter_value = parameter_index + len(search_parameter) + 1
attribute_separator_index = url_parametros.find('&', index_parameter_value)
if attribute_separator_index == -1:
    paremeter_value = url_parametros[index_parameter_value:]
else:
    paremeter_value = url_parametros[index_parameter_value:attribute_separator_index]

print(paremeter_value)