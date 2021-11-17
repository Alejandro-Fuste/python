# In python there are NO primitives: only objects
from abc import ABC, abstractmethod


# my_small_number = 1
# print(type(my_small_number))
#
# another_small_number = 1.1
# print(type(another_small_number))

# Most common data type string, number, float, boolean

# Classes

# class MyClass:
#     # you can have state and behavior in a class
#     # you set the state of the objects..you will create
#
#     # dunder method-you're meant to change it
#     def __init__(self):
#         print("this is run every time")


# class SetState:
#     def __init__(self, string_value: str, int_value: int):
#         self.string_value = string_value
#         self.int_value = int_value
#
# my_set_state_obj = SetState("my string", 2)
# print(my_set_state_obj.string_value, my_set_state_obj.int_value)


# class HasFunction:
#     def __init__(self, string_value: str, int_value: int):
#         self.string_value = string_value
#         self.int_value = int_value
#
#     def get_my_string(self):
#         return self.string_value
#
# my_class = HasFunction("new string", 5)
# print(my_class.get_my_string())

# Abstract Class

# For DRY, write one general class and implement specific versions using the abstract class

# class AbstractClass(ABC):
#
#     @abstractmethod
#         def my_abstract_method(self):
#             pass


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self):
        pass


class Adult(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def speak(self):
        return "Hello! My name is {} and I am {} years old".format(self.name, self.age)

adult = Adult("Eric", 127)
print(adult.speak())

