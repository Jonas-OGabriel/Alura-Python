from collections import Counter

class AluraCollections:

    def __init__(self, text_base):
        self.text_base = text_base.lower()
        self.list_most_common()
    
 
    def __str__(self):
        return str(self.char_percentage())


    def char_counter(self):
        for char in self.text_base:
            char_counter = Counter(self.text_base)
        return char_counter

    def char_percentage(self):
        char_counter_sum = sum(self.char_counter().values())
        char_list = self.char_counter()
        char_percentage = [(letter, frequency / char_counter_sum) for letter, frequency in char_list.items()]
        return char_percentage
    
    def list_most_common(self, quantity = 10):
        char_percentage = self.char_percentage()
        list_length = int(input('Digite quantos itens deseja verificar: '))
        
        if list_length == '':
            list_length = quantity
        
        most_common_itens = Counter(dict(char_percentage)).most_common(list_length)
        
        for char, value in most_common_itens:
            print('Letra: {} aparece {:.2f}%'.format(char, value * 100))

    

#_____TEST ZONE_____
def code_test():
    test = AluraCollections('Olá, este é meu texto de teste para fixar o conteúdo aprendido na Alura')

if __name__ == "__main__":
    code_test()
    
