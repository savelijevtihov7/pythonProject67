# indicies = []
# target = int(input())
# nums = []
# len_nums = int(input())
# for i in range(len_nums):
#     nums.append(int(input()))
#
# for i in len(nums):
#     c = i+1
#     while c != len(nums) - 1:
#         if (nums[i] + nums[c]) == target:
#             indicies.append(i)
#             indicies.append(c)
#         else:
#             c += 1
#
# print(indicies)

# users = {}
# count_users = int(input('Введите количество пользователей'))
# for i in range(count_users):
#     users.setdefault('Names', []).append(input('Введите имя пользователя'))
#     users.setdefault('Ages', []).append(int(input('Введите возраст пользователя')))
#     users.setdefault('Cities', []).append(input('Введите город пользователя'))
#
# print(users)
#
# def avg_age(dict):
#     return (sum(dict['Ages']) / len(dict['Names']))
###$$$
class Pet:

    def __init__(self, name, hunger):
        self.name = name #Имя питомца
        self.hunger = hunger #Уровень голода

    def eat(self):
        if self.hunger > 0:
            self.hunger -= 10
            print(f"{self.name} поел. Голод теперь {self.hunger}")
        else:
            print(f"{self.name} не хочет есть!")

    def say_hello(self):
        print(f"Привет! Меня зовут {self.name}, я чувствую себя отлично")

barcik = Pet("Барсик", 50)

sharik = Pet("Шарик", 80)

barcik.eat()
sharik.eat()
barcik.eat()

sharik.say_hello()
