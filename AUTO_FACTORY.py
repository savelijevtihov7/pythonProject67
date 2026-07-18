class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        self.history = []
    def deposit(self,amount):
        self.balance += amount
        self.history.append(f"Пополнение +{amount}. Баланс: {self.balance + amount}")
        return f"Клиент {self.owner} положил {amount} денег на счет, теперь его баланс составляет {self.balance}"
    def withdraw(self,amount):
        self.balance -= amount
        self.history.append(f"Снятие денег -{amount}. Баланс: {self.balance - amount}")
        return f"Клиент {self.owner} снял {amount} денег со счета, теперь его баланс составляет {self.balance}"
    def show_balance(self):
        return f"Баланс клиента {self.owner} составляет {self.balance}"
    def money_transfer(self,other_bank_account,amount):
        if self.balance >= amount:
            self.balance -= amount
            self.history.append(f"Перевод {other_bank_account.owner} прошел успешно. Ваш баланс составляет: {self.balance - amount}")
            return f"{self.owner} перевел деньги {other_bank_account.owner} в размере {amount}"
        else:
            self.history.append(f"Перевод {other_bank_account.owner} не удался. Недостаточно средств")
            return 'Недостаточно средств'

Ivan = BankAccount('Иван', 1_200_000)
Saveliy = BankAccount('Савелий', 120_000_000)

print(Saveliy.deposit(100_000))
print(Saveliy.money_transfer(Ivan,1_0000000000000_00000000000))
print(Saveliy.money_transfer(Ivan, 100_000))
print(Saveliy.history)