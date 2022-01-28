from cpf_cnpj import Document

cpf = '22936850800'
objeto_cpf = Document.get_document_type(cpf)
print(objeto_cpf)

cnpj = '35379838000112'
objeto_cnpj = Document.get_document_type(cnpj)
print(objeto_cnpj)