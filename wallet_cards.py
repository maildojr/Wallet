
class cards:
    all_cards = []

    def __init__(self, name, number, duedate,expdate, limit):
        self.name = name
        self.number = number
        self.duedate = duedate
        self.expdate = expdate
        self.limit = limit
        cards.all_cards.append([name,number, duedate, expdate, limit])
