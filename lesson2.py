# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

#
# def notebook():
#     todo_list = []
#
#     def add_todo(todo):
#         todo_list.append(todo)
#         print(todo_list) #return(todo_list)
#
#
#     return add_todo
#
#
# do = notebook()
# print(do("homework"))
# print(do("dz"))

#_______________________________________
# def notebook():
#     todo_list = []
#
#
#     def get_all(str):
#         todo_list.append(str)
#         for i in todo_list:
#              print(i)
#
#     return get_all
#
#
# r = notebook()
# print(r("dz"))
# print(r("hv"))
# print(r("hz"))

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція
# продекорована цим декоратором, та буде виводити це значення після виконання функцій

# def decor(func):
#     def inner(*args, **kwargs):
#         inner.count += 1
#         return func(*args, **kwargs)
#
#
#     inner.count = 0
#     return inner
#
#
#
#
# @decor
# def func1():
#     print("func1")
#
# @decor
# def func2():
#     print("func2")
#
#
# func1()
# func2()
# func1()
#
# print('counter:', func1.count)
# print('counter:', func2.count)

#_____________________

# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки
# (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'


#
# num = int(input("enter number: "))
#
# print(str(num//100 + num//10%10 + num%10))
























