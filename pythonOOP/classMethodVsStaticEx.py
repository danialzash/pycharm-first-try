"""
A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method can’t access or modify it.
In general, static methods know nothing about the class state.
They are utility-type methods that take some parameters and work upon those parameters.
On the other hand class methods must have class as a parameter.
We use @classmethod decorator in python to create a class method,
and we use @staticmethod decorator to create a static method in python.
"""

from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18


person1 = Person("Mahyar", 32)
person2 = Person.fromBirthYear("Hassan", 2004)

print(person1.age)
print(person2.age)
