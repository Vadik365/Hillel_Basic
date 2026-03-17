##### 4.1 ###### Перемістити всі нулі до кінця списку
nums = [2, 0, 4, 30, 0, 43, 65]
zero = []
no_zero = []

for num in nums:
    if num == 0:
        zero.append(num)
    else:
        no_zero.append(num)
new_list = no_zero + zero
print(new_list)

##### 4.2 ###### Знайти суму елементів із парними індексами
elements = [0, 1, 7, 2, 4, 8]
if len(elements) == 0:
    print(0)
else:
    sum_index = 0
    for index in range(0, len(elements), 2):
        sum_index += elements[index]
    result = sum_index * elements[-1]
    print(result)

##### 4.3 ######
import random

first_lst = []
for i in range(random.randint(3,10)):
    first_lst.append(random.randint(1,100))
second_lst = [first_lst[0], first_lst[2], first_lst[-2]]
print(first_lst)
print(second_lst)