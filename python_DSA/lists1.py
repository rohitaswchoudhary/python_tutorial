list1= ['physics', 'chemistry', 2002, 1997, 2006]
list2 = [1,2,3,4,5]

# accessing list elements

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])


print("----------------------------------------------------")

# updating list elements

list2[2] = 30

print("new value of list2[2]: ", list2[2])


print("----------------------------------------------------")

# deleting list elements

del list1[2]

print("after deleting list1[2]: ", list1)


print("----------------------------------------------------")

# length of list

print(len(list1))

# concatenating lists

print(list1+list2)

# checking membership

print(30 in list2)