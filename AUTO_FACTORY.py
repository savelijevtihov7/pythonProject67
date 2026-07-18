# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance = balance
#         self.history = []
#     def deposit(self,amount):
#         if amount <= 0:
#             return 'Сумма должна быть положительной'
#         self.balance += amount
#         self.history.append(f"Пополнение +{amount}. Баланс: {self.balance + amount}")
#         return f"Клиент {self.owner} положил {amount} денег на счет, теперь его баланс составляет {self.balance}"
#     def withdraw(self,amount):
#         if amount <= 0:
#             return 'Сумма должна быть положительной'
#         self.balance -= amount
#         self.history.append(f"Снятие денег -{amount}. Баланс: {self.balance - amount}")
#         return f"Клиент {self.owner} снял {amount} денег со счета, теперь его баланс составляет {self.balance}"
#     def show_balance(self):
#         return f"Баланс клиента {self.owner} составляет {self.balance}"
#     def money_transfer(self,other_bank_account,amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             other_bank_account.balance += amount
#             self.history.append(f"Перевод {other_bank_account.owner} прошел успешно. Ваш баланс составляет: {self.balance - amount}")
#             other_bank_account.history.append(f"Перевод от {self.owner} в размере {amount}. Ваш баланс составляет: {other_bank_account.balance + amount}")
#             return f"{self.owner} перевел деньги {other_bank_account.owner} в размере {amount}"
#         else:
#             self.history.append(f"Перевод {other_bank_account.owner} не удался. Недостаточно средств")
#             return 'Недостаточно средств'
#     def show_history(self):
#         ba = []
#         for operation in self.history:
#             ba.append(operation)
#         return ba
#
# Ivan = BankAccount('Иван', 1_200_000)
# Saveliy = BankAccount('Савелий', 120_000_000)
#
# print(Saveliy.deposit(100))
# print(Saveliy.money_transfer(Ivan,1_0000000000000_00000000000))
# print(Saveliy.money_transfer(Ivan, 100_000))
# print(Saveliy.show_history())
# print(Ivan.show_history())

class employee:
    def __init__(self,name,age,hometown,salary,grade):
        self.name = name
        self.age = age
        self.hometown = hometown
        self.salary = salary
        self.grade = grade

    def discussion_of_working_conditions(self):
        if (self.grade == 'junior' and self.salary < 100_000) or (self.grade == 'middle' and self.salary < 250_000) or (self.grade == 'senior' and self.salary < 500_000):
            return f"Сотрудник {self.name} просит увеличит свою заработную плату, или повысить его в должности, так как считает, что зарплата {self.salary} не соответсвует его грейду {self.grade}"
        else:
            return f"Сотрудник {self.name} доволен рабочими условиями"

    def rest_days(self):
        if self.age > 40:
            return f"Сотрудник {self.name} просит увеличить время отпуска, так как нагрузка на работе его не устраивает"
        else:
            return f"Сотрудник {self.name} доволен количеством отдыха и жаждет работать над проектом с полной силой!"

class developer(employee):
    def drink_coffee(self):
        return f"Сотрудник {self.name} заказал раф на лавандовом молоке и потребовал приобрести упаковку печенья на его рабочее место"
    def work(self):
        return f"Сотрудник {self.name} приступил к работе над FAST API проектом"

class engineer(employee):
    def drink_coffee(self):
        return f"Сотрудник {self.name} заказал двойной американо и потребовал сделать его заказ как можно быстрее в связи со сбоем электричества"
    def work(self):
        return f"Сотрудник {self.name} приступил к работе над сгоревшей проводкой"
Saveliy = developer('Савелий',18,'Брянск', 500_000, 'middle')
Vasiliy = engineer('Василий', 67, 'Краснодар', 100_000, 'senior')
employees = [Saveliy,Vasiliy]
for man in employees:
   print(man.work())