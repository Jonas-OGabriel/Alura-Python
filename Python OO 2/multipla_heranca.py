#Primeira classe mãe
class Worker:
    
    def __init__(self, nome):
        self.nome = nome
    
    def register_hour(self, worked_hours):
        print("Horas registradas")

    def show_tasks(self):
        print("Fez muita coisa...")
#------------------------------------

#Mixin
class Hipster:
    def __str__(self):
        return "Nome: {}".format(self.nome)
#------------------------------------

#Classes herdeiras de Worker 
class Caelum(Worker):
    
    def show_tasks(self):
        print("Fez muita coisa, Caelumer!")
    
    def search_month_course(self, mes=None):
        print("Mostrando cursos - {}".format(mes) if mes else "Mostrando cursos desse mes")
    
class Alura(Worker):

    def show_tasks(self):
        print("Fez muita coisa, Alurete!")
    
    def search_question_without_answer(self):
        print("Mostrando perguntas não respondidas do forum")
#------------------------------------

#Classes herdeiras de Caelum / Alura
class Junior(Alura):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass
#------------------------------------

#Teste de codigo
def test_function():
    
    junior1 = Junior('Jr 1')
    junior1.search_question_without_answer()
    print(junior1)
    print("End Junior")

    pleno1 = Pleno('Pleno 1')
    pleno1.search_question_without_answer()
    pleno1.search_month_course()
    pleno1.show_tasks()
    print(pleno1)
    print("End Pleno")

if __name__ == "__main__":
    test_function()
#------------------------------------