# power table of any number using anonymous function
# 2023-04-25 17:42:06
term = int(input("enter the number of terms: "))
n = int(input("enter the number to find the power table:"))

result = list(map(lambda x: n**x, range(term)))
print(result)

for i in range(term):
    print(f"{n}^{i} is", result[i])

    