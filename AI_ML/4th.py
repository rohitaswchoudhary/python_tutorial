# power table of any number using anonymous function
# 2023-04-25 17:42:06
# term = int(input("enter the number of terms: "))
# n = int(input("enter the number to find the power table:"))

term = 5
n = 5

result = list(map(lambda x: n**x, range(term)))
print(result)

for i in range(term):
    print(f"{n}^{i} is", result[i])

num = range(1,term,1)
print(num)
print(type(num))

sentence = "A quick brown fox jumps over the lazy dog.       "
number = "5"
print(sentence.upper())
print(sentence.lower())
print(sentence.partition("jumps"))
print(sentence.find("z"))
print(sentence, sentence)
print(sentence.rstrip(),sentence)
print(sentence.split("o"))
print(number.isnumeric())
print(sentence.isnumeric())



