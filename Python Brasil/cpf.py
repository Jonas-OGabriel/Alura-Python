from validate_docbr import CPF

class Cpf:
    
    def __init__(self, doc_number):
        doc_number_str = str(doc_number)
        if self.validate_cpf(doc_number_str):
            self.cpf = doc_number_str
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.format_visualization_cpf()
    
    def validate_cpf(self, doc_number_str):
        if len(doc_number_str) == 11:
            validator = CPF()
            return validator.validate(doc_number_str)
        else:
            raise ValueError('Digitos insuficientes')

    def format_visualization_cpf(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)