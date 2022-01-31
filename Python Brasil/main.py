from cpf_cnpj import Document
from telefones import Telefone
from datas import Date
""" 
cpf = '22936850800'
objeto_cpf = Document.get_document_type(cpf)
print(objeto_cpf)

cnpj = '35379838000112'
objeto_cnpj = Document.get_document_type(cnpj)
print(objeto_cnpj)
"""
telefone = '551151096589'
objeto_telefone = Telefone(telefone)
print(objeto_telefone)


""" 
cadastro = Date()
print(cadastro.sing_in_month())
 """