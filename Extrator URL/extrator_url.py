import re
from decimal import Decimal

class ExtratorURL:

    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.validate_url()
        self._dolar_value = Decimal('5.50')
        self.set_output()

    def sanitize_url(self, dirt_url):
        if type(dirt_url) == str:
            return dirt_url.strip()
        else:
            return ""
    
    def validate_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        
        default_url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = default_url_pattern.match(self.url)

        if not match:
            raise ValueError("A URL NÃO é válida")  

    def get_base_url(self):
        separator_index = self.url.find('?')
        base_url = self.url[:separator_index]
        return base_url
    
    def get_parameter_url(self):
        separator_index = self.url.find('?')
        parameter_url = self.url[separator_index+1:]
        return parameter_url

    def get_parameter_value(self, parameter_name):
        parameter_url = self.get_parameter_url()
        
        initial_parameter_index = parameter_url.find(parameter_name)
        end_parameter_index = initial_parameter_index + len(parameter_name) + 1
        
        attribute_separator_index = parameter_url.find('&', end_parameter_index)
        
        if attribute_separator_index == -1:
            parameter_value = parameter_url[end_parameter_index:]
        else:
            parameter_value = parameter_url[end_parameter_index:attribute_separator_index]

        return parameter_value

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros da URL: " + self.get_parameter_url() + "\n" + "URL Base: " + self.get_base_url()

    def __eq__(self, other):
        return self.url == other.url
    
    def get_conversion_value(self):
        if self.get_parameter_value('moedaOrigem') == "dolar":
            final_value = Decimal(self.get_parameter_value('quantidade')) * self._dolar_value
        else:
            final_value = Decimal(self.get_parameter_value('quantidade')) / self._dolar_value
        return Decimal(final_value)
    
    def set_output(self):
        print("A moeda origem é: $ {:0.2f} {}(s)".format(float(self.get_parameter_value('quantidade')), self.get_parameter_value('moedaOrigem')))
        print("Sendo covertido para: $ {:0.2f} {}(s)".format(self.get_conversion_value(), self.get_parameter_value('moedaDestino')))
        
        

def test(test_url = None):
    test = ExtratorURL(test_url)
    """ 
    #Esta parte é apenas para testar pontos específicos do código no decorrer das aulas

    print("A moeda origem é:")
    print(test.get_parameter_value('moedaOrigem'))
    print("A moeda destino é:")
    print(test.get_parameter_value('moedaDestino'))
    
    #Para comparar se está certo
    print(len(test)==len("https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"))

    #Para testar __str__
    print(test)

    #Para testar __eq__
    test2 = ExtratorURL(test_url)
    print(test == test2)
    print(test is test2) # 'is' utiliza-se para saber se a IDENTIDADE de ambos valore é igual e.g: print( 1 is True) 
     """




if __name__ == '__main__':
    #Para testar uma url: "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"
    test("https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100")