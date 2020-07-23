# creating a set:

thisset = {"apple", "banana", "cherry"}
print(thisset)

# access items in sets:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# change items

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# adding multiple items to a set.

thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)

# length of set.

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# remove item
# If the item to remove does not exist, remove() will raise an error.

thisset.remove("banana")

print(thisset)

# If the item to remove does not exist, discard() will NOT raise an error.

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# pop
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# join two set.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
