from abc import ABC
from abc import abstractmethod


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
# class Cinderella(Human):
#
#      def __init__(self, name, age, foot_size, cindarellas_list):
#          super().__init__(self, name, age)
#          self.foot_size = foot_size
#
#      def total(self):
#          return len(Prince.cindarellas_list)
#
#
# class Prince(Human, Cinderella):
#     def __init__(self, name, age, foot_size):
#         super().__init__(name, age, foot_size)
#
#     the_one = 36
#
#     def tarantino(self, the_one):
#
#         cindarellas_list = dict(input("enter cindarella's name and feet sizes"))
#
#         for value in cindarellas_list.values():
#             if value == the_one:
#                 print("The One is found!")
#             else:
#                 print("Спасибо, я еще похожу, посмотрю")
#
#
#
# h = Human()
# c = Cinderella()
# p = Prince()




# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку
#  чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()

# для перевірки ксассів використовуємо метод isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False


# class Printable(ABC):
#
#     @abstractmethod
#     def print(self):
#         pass
#
#
#
# class Book(Printable):
#     def __init__(self, name):
#         pass
#
#
#
# class Magazine(Printable):
#     def __init__(self, name):
#         pass
#
#
# class Main(Printable, Book, Magazine):
#     printable_list = []
#     item = input("book or a magazin or...?")
#
#     def add(self, item, printable_list):
#         if isinstance(item, Book) or isinstance(item, Magazine):
#             printable_list.append(item)
#         else:
#             pass
#
#
#     def show_all_books(self, item, printable_list):
#         def print(self):
#             for i in printable_list:
#                 if isinstance(item, Book):
#                     print(i)
#
#     def show_all_magazines(self, item, printable_list):
#         def print(self):
#             for i in printable_list:
#                 if isinstance(item, Magazine):
#                     print(i)
#
#






