from project import MainDish


class Salmon(MainDish):
    GRAMS = 22
    def __init__(self,name:str,price:float):
        # MainDish.__init__(self,name,price,self.GRAMS)
        super().__init__(name, price, self.GRAMS)

