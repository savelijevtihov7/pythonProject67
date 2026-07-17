class AUTO:

    def __init__(self,name,max_speed,horse_power,cost):
        self.name = name
        self.max_speed = max_speed
        self.horse_power = horse_power
        self.cost = cost

    def IsItPowered(self):
        if self.horse_power > 299:
            return f"Автомобиль {self.name} будет подвержен повышенному налогооблажению из-за высокой мощности"
        else:
            return f"Автомобиль {self.name} повышенному налогооблажению не подвержен"

    def IsItExpensive(self):
        if self.cost > 3_000_000:
            return f"В связи с высокой стоимостью автомобиля {self.name}: {self.cost}, он будет ввезен с большой наценкой"
        else:
            return f"Наценка на автомобиль {self.name} оптимальна для ввоза в РФ"

    def IsItFast(self):
        if self.max_speed > 260:
            return f"Автомобиль {self.name} является суперкаром"
        else:
            return f"Автомобиль {self.name} является автомобилем бизнес класса"

class BMW(AUTO):
    def CAR_RATING(self):
        return f"Автомобиль {self.name} разгоняется до 100 быстрее конкурентов, но обладает меньшей устойчивостью при прохождении поворотов"

class MERCEDES(AUTO):
    def CAR_RATING(self):
        return f"Автомобиль {self.name} обладает наименьшей разгонной динамикой среди конкурентов, но превосходит их по уровню комфорта"


First_Car = BMW("BMW M5 G90", 290, 801, 21_000_000)
Second_Car = MERCEDES('MERCEDES E63 AMG', 276, 630, 12_000_000)

print(First_Car.CAR_RATING())
print(Second_Car.CAR_RATING())
print(First_Car.IsItFast())
print(Second_Car.IsItFast())
print(First_Car.IsItPowered())
print(Second_Car.IsItPowered())