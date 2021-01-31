list1=[1,2,3]
print(list1)

list12= [4.5,'string',3,[2,4,6]]            # mixed lists
print(list12)

print(list12[0])
print(list12[1])
print(list12[2])
print(list12[3])
list12.append(10)
print(list12)

list12.insert(1,100)
print(list12)
list12.insert(0,'rohit')
print(list12)

list12.remove(100)
print(list12)

list12.reverse()

print(list12)

list13=[8,5,2,3,6,9,7,4,5,6,8,9,1,2,56]
list13.sort()
print(list13)

# indexing

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# negative indexing

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# range of indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# change item value

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)



# zipped lists

l1 = [1,2,3,4,5]
l2 = ["one","two","three","four","five"]

zipped = list(zip(l1,l2))
print(zipped)

unzipped = list(zip(*zipped))
print(unzipped)

items = ["apple","banana","oranges"]
counts = [4,10,12]
prices = [20,30,100]

sentences = []
for (item,count,price) in zip(items,counts,prices):
    item,count,price = str(item),str(count),str(price)
    sentence = "I brought "+count+ " "+item+ " at ₹"+price +" each."
    sentences.append(sentence)

print(sentences)

all_lists = []
for all in (list1,list12,list13,thislist,sentences,l1,l2,zipped,unzipped,items,counts,prices):
    all_lists.append(all)

print(all_lists)


shopping_list = ['milk', 'yoghurt', 'egg', 'butter', 'bread', 'bananas']
cart = []
while shopping_list != []:
    article = shopping_list.pop()  
    cart.append(article)
    print(article, shopping_list, cart)

print("shopping_list: ", shopping_list)
print("cart: ", cart)


# Shallow and Deep Copy
x = 3
y = 4
print(id(x),id(y))
print("memory location id of x:",id(x),"\nmemory location id of y:",id(y))

colours1 = ["red", "blue"]
colours2 = colours1
print(colours1, colours2)

print(id(colours1),id(colours2))      # the id will appear same in both cases.

# Now we want to see, what happens, if we assign a new object to colours2. 
# As expected, the values of colours1 remain unchanged. 
# Like it was in our example in the chapter "Data Types and Variables",
#  a new memory location had been allocated for colours2, as we have assigned a completely new list, 
# i.e. a new list object to this variable.

colours1 = ["red", "blue"]
colours2 = colours1
print(id(colours1), id(colours2))

colours2 = "green"
print(colours1)

print(colours2)

# print(help(list.copy))

person1 = ["Swen", ["Seestrasse", "Konstanz"]]
person2 = person1.copy()

person2[0] = "rohit"
print(person2)
print( "        ------------------------------                "   )

# deep copy of lists.

from copy import deepcopy
person1 = ["Swen", ["Seestrasse", "Konstanz"]]

person2 = deepcopy(person1)
person2[0] = "Sarah"

person2[1][0] = "Bücklestrasse"
print(person1,"\n",person2)
