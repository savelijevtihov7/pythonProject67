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
my_dict = {}
names = ['Vasya', 'Petya', 'Gulia']
ages = [12, 13, 47]
cities = ['Moscow', 'Bryansk', 'Berlin']
my_dict.update({'names': names, 'ages': ages, 'cities': cities})
print(my_dict)