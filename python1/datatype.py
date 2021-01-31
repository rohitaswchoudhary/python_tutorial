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
from typing import Sequence


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

# bytes
# the bite object is a Sequence of small integers. the elements of a byte are in the range 0 to 255, 
# corrosponding to ASCII character.
s= "Rohitasw Choudhary,rohit"
s_bytes = s.encode("utf-8")
print(s_bytes)
