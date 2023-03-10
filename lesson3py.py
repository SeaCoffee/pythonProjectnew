# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

# class Rectangle():
#     """Клас прямокутник"""
#     def __init__(self, x, y, *args):
#         """сторони прямокутника"""
#         self.x = x
#         self.y = y
#         self.sides = args

    #
    # def sum(self):
    #     """площа прямокутника"""
    #     square = self.x * self.y
    #     return square
    #
    # def __add__(self, other):
    #     """сумма площин двох екземплярів ксласу"""
    #     return self.x * self.y + other.x * other.y
    #
    # def __sub__(self, other):
    #     """різниця площин двох екземплярів ксласу"""
    #     return self.x * self.y - other.x * other.y
    #
    # def __eq__(self, other):
    #     """== площин на рівність"""
    #     r1_square = self.x * self.y
    #     r2_square = other.x * other.y
    #     if r1_square == r2_square:
    #         return True
    #     else: return False
    #
    #
    # def __le__(self, other):
    #     """>, < меньше більше"""
    #     r1_square = self.x * self.y
    #     r2_square = other.x * other.y
    #     if r1_square <= r2_square:
    #         return True
    #     else: return False
    #
    #
    # def __gt__(self, other):
    #     """>, < меньше більше"""
    #     r1_square = self.x * self.y
    #     r2_square = other.x * other.y
    #     return r1_square > r2_square
    #
    # def __ne__(self, other):
    #     """!= площин на рівність"""
    #     r1_square = self.x * self.y
    #     r2_square = other.x * other.y
    #     if r1_square != r2_square:
    #         return True
    #     else:
    #         return False

#     def __len__(self):
#         return len(self.sides)
#
#
#
#
# rectangle1 = Rectangle(5,25)
# rectangle2 = Rectangle(6,21)
#
# print(len(rectangle1))



# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка,
# а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість
# створених екземплярів классу
# також має бути метод классу який буде виводити це значення

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Prince(Human):
#     the_one = 36
#
#
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#
#     def tarantino(self, the_one):
#
#         cindarellas_list = dict(input("enter cindarella's name and feet sizes"))
#
#         for value in cindarellas_list.values():
#             if value == the_one:
#                 print("The One")
#             else:
#                 print("Спасибо, я еще похожу, посмотрю")
#
#
#
# class Cinderella(Human, Prince):
#
#
#     def __init__(self, name, age,  cindarellas_list, the_one):
#         super().__init__(self, name, age, cindarellas_list, the_one)
#
#         def cinda_counter(self, cindarellas_list):
#             total = len(cindarellas_list)
#             print(total)
#




