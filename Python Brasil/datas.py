from datetime import datetime

class Date:

    def __init__(self):
        self.sing_in_date = datetime.today()
    
    def sing_in_month(self):
        month_list = [
            'Jan', 'Fev', 'Mar', 
            'Abr', 'Mai', 'Jun', 
            'Jul', 'Ago', 'Set', 
            'Out', 'Nov', 'Dez'
            ]
        sing_in_month = self.sing_in_date.month
        return month_list[sing_in_month - 1]