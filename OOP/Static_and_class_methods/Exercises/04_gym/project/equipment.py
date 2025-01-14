from project import ClsMixin


class Equipment(ClsMixin):


    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()
        self.increments_id()




    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

