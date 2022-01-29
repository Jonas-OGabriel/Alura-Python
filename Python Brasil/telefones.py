from sympy import re


import re

class Telefone():

    def __init__(self, phone_number):
        if self.validate_telephone(phone_number):
            self.number = phone_number
        else:
            raise ValueError('Numero invalido')

    def validate_telephone(self, phone_number):
        default_format = '[0-9]{2,3}[0-9]{2}[0-9]{4,5}[0-9]{4}'
        if re.findall(default_format, phone_number):
            return True 

