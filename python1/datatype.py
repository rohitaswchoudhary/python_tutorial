'''
built in data types 

text type: str
numeric types: int, float, complex
sequence types: tuple, list, range
mapping types: dict
set types: set , frozenset
boolean types: bool
binary types: bytes, bytearray, memoryview
'''
# You can get the data type of any object by using the type() function:
x=10
y=10.5
z="rohit"
k=3+5j
print(x,type(x))
print(y,type(y))
print(z,type(z))
print(k,type(k))


# multi line string
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)