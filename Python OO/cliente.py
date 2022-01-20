
class Cliente:

    def __init__(self, client_name):
        self.__client_name = client_name
    
    @property
    def client_name(self):
        print("Chamando @property client_name()")
        return self.__client_name.title()
    
    @client_name.setter
    def client_name(self, new_name):
        print("Chamando Setter de name()")
        self.__client_name = new_name