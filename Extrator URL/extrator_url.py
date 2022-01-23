class ExtratorURL:

    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.validate_url()

    def sanitize_url(self, dirt_url):
        if type(dirt_url) == str:
            return dirt_url.strip()
        else:
            return ""
    
    def validate_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

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


def test(test_url = None):
    test = ExtratorURL(test_url)
    print("A moeda origem é:")
    print(test.get_parameter_value('moedaOrigem'))
    print("A moeda destino é:")
    print(test.get_parameter_value('moedaDestino'))




if __name__ == '__main__':
    #Para testar uma url: "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
    test()