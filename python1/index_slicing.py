digits1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(digits1[2])
print(digits1[-2])
print()
print()

print(digits1[0:3])

print()

name= "Rohitasw choudhary"
print(name[:5])

print()




digits=[0,1,2,3,4,5,6,7,8,9]

####Indexing

print(digits[0])
print(digits[5])

print(digits[-2])
print([-10])

print([-len(digits)])
print([len(digits)-1])

print(digits[2:6])
print(digits[1:10:2])
print(digits[::-1])

######Slicing

for i in range(len(digits)):
    print(digits[0:i])

window_size=3
for i in range(len(digits)-(window_size-1)):
    print(digits[i:i+window_size])