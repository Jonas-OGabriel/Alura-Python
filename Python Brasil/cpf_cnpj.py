from validate_docbr import CPF, CNPJ

class Document():

    @staticmethod
    def get_document_type(document_number):
        if len(document_number) == 11:
            return DocCPF(document_number)
        elif len(document_number) == 14:
            return DocCNPJ(document_number)
        else:
            raise ValueError('Quantidades de digitos invalido')

class DocCPF():

    def __init__(self, document_number):
        if self.validate_cpf(document_number):
            self.cpf = document_number
        else:
            raise ValueError('CPF invalido')

    def __str__(self):
        return self.format_presentation()


    def validate_cpf(self, document_number):
       validator = CPF()
       return validator.validate(document_number)
    
    def format_presentation(self):
        mask = CPF()
        return mask.mask(self.cpf)

class DocCNPJ():
    
    def __init__(self, document_number):
        if self.validate_cnpj(document_number):
            self.cnpj = document_number
        else:
            raise ValueError('CPF invalido')

    def __str__(self):
        return self.format_presentation()


    def validate_cnpj(self, document_number):
       validator = CNPJ()
       return validator.validate(document_number)
    
    def format_presentation(self):
        mask = CNPJ()
        return mask.mask(self.cnpj)