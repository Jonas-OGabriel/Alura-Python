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
        if self.doc_type == 'cpf':
            return self.format_visualization_cpf()
        elif self.doc_type == 'cnpj':
            return self.format_visualization_cnpj()
    
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
    
    def format_visualization_cnpj(self):
        cnpj_mask = CNPJ()
        return cnpj_mask.mask(self.cnpj)