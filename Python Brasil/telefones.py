from sympy import re


import re

class Telefone():
    
    #First Definitions
    @staticmethod
    def default_number_format():
        return '([0-9]{2,3})?([0-9]{2})([9]{1})?([0-9]{4})([0-9]{4})'

    def default_regex(self):
        return re.search(self.default_number_format(), self.number)

    
    #Special Functions
    def __init__(self, phone_number):
        if self.validate_telephone(phone_number):
            self.number = phone_number
        else:
            raise ValueError('Numero invalido')

    def __str__(self):
        return self.print_mask()

    
    #Validation Functions
    def validate_telephone(self, phone_number):
        if len(phone_number) <= 14 and re.findall(self.default_number_format(), phone_number):
            return True
     
    
    #Formatations Functions
    def format_country_number(self):
        number_mask = self.default_regex()
        if not number_mask.group(1):
            country_code = '55'
        else:
            country_code = number_mask.group(1)
        return country_code
        
    def format_mobile_id(self):    
        number_mask = self.default_regex()
        if not number_mask.group(3):
            mobile_id = ''
        else:
            mobile_id = number_mask.group(3)
        return mobile_id

    #Output Function
    def print_mask(self):
        number_mask = self.default_regex()
        return '+{} ({}) {}{}-{}'.format(
            self.format_country_number(),
            number_mask.group(2),
            self.format_mobile_id(),
            number_mask.group(4),
            number_mask.group(5),
        )


