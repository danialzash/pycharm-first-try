"""
Built-in data types

Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
"""

string1 = 'string'

number1 = 12
number2 = 12.4
number3 = 12 + 4j

list1 = ['1', '2']
tuple1 = tuple(('1', '2'))
range1 = range(10)

dict1 = {'key1': 'value1'}

set1 = set(('1', '2'))
set2 = frozenset(('1', '2'))

bool1 = False

byte1 = bytes(5)
byte2 = bytearray(5)
byte3 = memoryview(bytes(5))

print(type(string1))
print(type(number1))
print(type(number2))
print(type(number3))
print(type(list1))
print(type(tuple1))
print(type(range1))
print(type(set1))
print(type(set2))
print(type(bool1))
print(type(byte1))
print(type(byte2))
print(type(byte3))