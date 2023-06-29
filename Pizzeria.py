from Pizza import Pizza
from typing import List

class CartePizzeriaException:
    pass


class  Pizzeria:

    def __init__(self):
        self.pizzas: List[Pizza]=[]

    def isEmpty(self):
        return len(self.pizzas)==0
    
    def nb_pizza(self):
        return len(self.pizzas)
    def add(self,pizza:Pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self,pizza):
        try:
            self.pizzas.remove(pizza)
        except ValueError:
            raise CartePizzeriaException(f"{pizza} was not found.")