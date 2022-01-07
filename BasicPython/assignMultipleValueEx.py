"""
How to assign multiple values
"""

# 1.Assign values to multiple variables in one line
var1, var2, var3 = 'value1', 'value2', 'value3'

print(var1, var2, var3)

# 2.Assign the same value to multiple variables
var1 = var2 = var3 = "the same value"

print(var1, var2, var3)

# 3.Unpack collection of values in a list, tuple etc.
myList = ['value1', 'value2', 'value3']

var1, var2, var3 = myList

print(var1, var2, var3)

myTuple = ['value1-tuple', 'value2-tuple', 'value3-tuple']

var1, var2, var3 = myTuple

print(var1, var2, var3)