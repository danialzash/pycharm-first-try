"""
How lambda works in python
Lambda Syntax
"""


# lambda arguments : expression

def my_function(number):
    return lambda x: x * number


# make double functions
double_func = my_function(2)

# make triple function
triple_func = my_function(3)

print(double_func(10))
print(triple_func(10))

# how to use lambda
print(my_function(2)(3))
