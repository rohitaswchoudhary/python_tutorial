# 2023-04-20 17:57:06
# use of random module
import random

string = ["Rohit", "Satish","Pratik", "Rohitasw"]

r = random.choice(string)

print(r)


# swaping of two variables in python
x= int(input("enter value of x: "))
y = int(input("enter the value of y: "))

print(f"value of x:{x}, value of y:{y}")

temp = x
x = y
y = temp

print(f"value after swaping: x = {x}, y = {y}")

x, y = y, x

print(f"value after swaping: x = {x}, y = {y}")

