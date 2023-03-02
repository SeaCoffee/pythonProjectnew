# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4

#
# task_1 = input("enter anything")
# num_list = []
#
# for i in task_1:
#     if i.isdigit():
#         num_list += i
#         print(num_list, sep=",")



# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі


# task_2 = input()
# l = len(task_2)
# res_list = []
# i = 0
# while i < l:
#     s_int = ''
#     a = task_2[i]
#     while '0' <= a <= '9'
#         s_int += a
#         i += 1
#         if i < l:
#             a = task_2[i]
#         else:
#             break
#     i += 1
#     if s_int != '':
#         res_list.append(int(s_int))
#
# print(res_list)


# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# res_list = []
# greeting = 'Hello, world'
# greeting_2 = greeting.upper()
# for i in greeting_2:
#     res_list.append(i)
# print(res_list)

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
#

# for i in range (1,50):
#     if i % 2 != 0:
#         print(i**2)

#_________
# - створити функцію яка виводить ліст
# взагалі не зрозуміла завдання (???!)
#__________


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def large(arr):
#     max = arr[0]
#     for i in arr:
#         if i > max:
#            max = i
#     return max
#
#
# list1 = [1,2,3]
# result = large(list1)
# print(result)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше


# def func(*args):
#     return max(args)
#
# print(func(min(3,5,7,666)))

# - створити функцію яка повертає найбільше число з ліста
# - створити функцію яка повертає найменьше число з ліста
# - об"єднала

# def function_task(*args):
#     print(f'min number: {min(args)}, max number: {max(args)}')
# function_task(3,5,7,666)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def function_task(arr):
#     res = sum(arr)
#     return(res)
#
#
# function_task([3,5,7,666])

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# def function_task(arr):
#     res = sum(arr)
#     return(res / len(arr))
#
#
# function_task([3,5,7,666])

# 1)Дан list:

#list = [22, 3,5,2,8,2,-23, 8,23,5]

# - знайти мін число

# print(min(list))

# - видалити усі дублікати

# print(set(list))

# - замінити кожне 4 - те значення на 'X'

# for i in range(len(list)):
#     if list[i] % 4 == 0:
#         list[i] = 'X'
#
# print(list)

# for i in range(0, len(list), 4):
#      list[i] = 'X'
#      print(list)

#2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції


# count = int(input("Введите длину сторон: "))
# print("* " * count)
# for _ in range(count - 2):
#     print("* ", "  " * (count - 3), "* ")
#     print("* " * count)


# def print_square(N):
#     list(map(print, ['*' * N] * N))
# print_square(10)


# 3) вывести табличку множення за допомогою цикла while
#
# number = int(input ("Enter the number: "))
# count = 1
# # we are using while loop for iterating the multiplication 10 times
# print ("Number of multiplication table: ", number)
# while count <= 10:
#     number = number * 1
#     print (number, 'x', count, '=', number * count)
#     count += 1


# 4) переробити це завдання під меню
# це з hwhile має бути теж??? Мені не зовсім ясно що тут потрібно було робити...
# Ну типу меню з while...

# while True:
#     print("1. пункт ")
#     print("2. пункт")
#     print("3. пункт")
#     print("0. вийти из програми")
#     cmd = input("виберіть пункт: ")
#
#     if cmd == "1":
#         print("ви вибрали 1")
#
#     elif cmd == "2":
#         print("ви вибрали 2")
#
#     elif cmd == "3":
#         print("ви вибрали 1")
#     #
#     elif cmd == "0":
#         break
#     else:
#         print("Ви ввели абракадабру")













