list1=[1,2,3]
print(list1)

list12= [4.5,'string',3,[2,4,6]]
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





