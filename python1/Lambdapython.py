# A lambda function is a small anonymous function.
'''
A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression
The expression is executed and the result is returned:
'''
x = lambda a : a + 10
print(x(5))
print()

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
print()
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


