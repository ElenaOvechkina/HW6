class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}
class Position(Worker):
    def get_full_name(self):
        return f'{self.name}\n{self.surname}'

    def get_full_profit(self):
        return f"{sum(self._income.values())}"
p = Position('Иван', 'Иванов', 'Бухгалтер', '100000', '20000')
print(p.get_full_name())
print(p.position)
print(p.get_full_profit())