class копилка:

    def __init__(self, start):
        self.start = start
        self.popolnenia = []
        self.summ = self.start

    def __str__(self):
        return f"💰 В копилке: {self.summ}₽"

    def __repr__(self):
        return f"Копилка({self.summ})"

    def __call__(self, amount):
        self.summ = self.summ + amount
        self.popolnenia.append(amount)

    def __getitem__(self, key):
        return self.popolnenia[key]