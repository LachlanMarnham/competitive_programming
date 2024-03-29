class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name} {self.score}"

    @classmethod
    def comparator(cls, a, b):
        if a.score > b.score:
            return -1
        elif a.score == b.score:
            if a.name < b.name:
                return -1
            elif a.name > b.name:
                return 1
            else:
                return 0
        else:
            return 1
