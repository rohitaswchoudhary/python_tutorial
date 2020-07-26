# tuples cannot be edited
# stable structured data types
# it is similar to lists with some constrains

t = (1,2,3,4,5)
print(t[2])

credit_card1=(1234567891234567,"rohit",'11/22',123)
credit_card2=(1234123412341234,'rohitasw','11/23',456)

credit_cards=[credit_card1,credit_card2]
print(credit_cards)

thistuple = ("apple", "banana", "cherry")
print(thistuple)

print(thistuple[1])
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# you cannot add items to tuples.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# you cannot change items from tuple.

# but del keyword can delete the tuple completely.
'''
thistuple1 = ("apple", "banana", "cherry")
del thistuple1
print(thistuple1) #this will raise an error because the tuple no longer exists.
'''
# join two tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# tuple constructor

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
