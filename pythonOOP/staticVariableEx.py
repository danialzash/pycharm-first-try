


class CssStudent:
    stream = 'cse'
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

a = CssStudent('Rick', 1)
b = CssStudent('Morty', 2)

print(a.stream)
print(b.stream)

print(CssStudent.stream)

a.stream = 'eeeeeee'
CssStudent.stream = 'aaaaaaa'

print(a.stream)
print(b.stream)