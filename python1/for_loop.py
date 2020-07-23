for i in range(100):
    print([i,i+1])
print(i)
print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# looping through a string.

for x in "banana":
  print(x)

# break statement.
fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x=='banana':
        break

print("///////////////////////")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print("----------------")
# continue statement
# With the continue statement we can stop the current iteration of the loop, 
# and continue with the next:
fruits = ["apple", "banana", "cherry", "mango"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
print("::::::::::::::::::::::::")

# range() function.
for x in range(1,6):
  print(x)

print()
for x in range(2, 30, 3):
  print(x)

# nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

    
