"""
The word polymorphism means having many forms
Example of inbuilt polymorphic function is 'print'
print(len("string")) : 5
print(len([10, 20, 30])) : 3
"""


def add(x, y, z=0):
    return x + y + z


print(add(2, 3))
print(add(2, 3, 4))

class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
	country.capital()
	country.language()
	country.type()


class Bird():
    def intro(self):
        print("birds")
    def flight(self):
        print("birds can fly")

class Sparrow(Bird):
    def flight(self):
        print("Sparrow can fly")

class Ostrich(Bird):
    def flight(self):
        print("ostrich can't fly")

obj_bird = Bird()
obj_sparrow = Sparrow()
obj_ostrich = Ostrich()

obj_bird.flight()
obj_ostrich.flight()
obj_sparrow.flight()