from validate_docbr import CPF, CNPJ

class CpfCnpj:
    
    def __init__(self, doc_number, doc_type):
        doc_number_str = str(doc_number)
        self.doc_type = str(doc_type)
        if self.doc_type == 'cpf':
            if self.validate_cpf(doc_number_str):
                self.cpf = doc_number_str
            else:
                raise ValueError("CPF inválido")
        elif self.doc_type == 'cnpj':
            if self.validate_cnpj(doc_number_str):
                self.cnpj = doc_number_str
            else:
                raise ValueError("CNPJ inválido")
        else:
            raise ValueError('Valor Invalido')


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

    def validate_cnpj(self, doc_number_str):
        if len(doc_number_str) == 14:
            validator = CNPJ()
            return validator.validate(doc_number_str)
        else:
            raise ValueError('Digitos insuficientes')