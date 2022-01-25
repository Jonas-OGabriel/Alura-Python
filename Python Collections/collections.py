
def wrong_list():
    #Criando valores em variáveis diferentes, simulando uma "lista"
    example1 = 'Primeiro Valor'
    example2 = 'Segundo Valor'
    example3 = 'Terceiro Valor'

    print(example1)
    print(example2)
    print(example3)

def right_list():
    #Criando um lista em python
    example_list = ['Primeiro Valor', 'Segundo Valor', 'Terceiro Valor']
    example_list[0]
    example_list[1]
    example_list[2]

    print(type(example_list))
    print(len(example_list))

    print(example_list[0])
    print(example_list)


def modify_list():
    #Modificando uma lista
    example_list = ['Primeiro Valor', 'Segundo Valor', 'Terceiro Valor']
    print(example_list)

    example_list.append('Valor adicionado')
    example_list.append('Valor que será removido')
    print(example_list)

    example_list.remove('Valor que será removido')
    print(example_list)


def test():
    #wrong_list()
    #right_list()
    modify_list()

if __name__ == "__main__":
    test()