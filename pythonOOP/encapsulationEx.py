


class Base:
    def __init__(self):
        # Protected member
        self._a = 2

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("calling protected member of base class:", self._a)

        #change protected member value in subclass
        self._a = 3
        print("calling protected member outside class:", self._a)


obj1 = Derived()
obj2 = Base()

print("Accessing protected member", obj1._a)
print("Accessing protected member", obj2._a)