import re

text="A random string. Rohitasw Choudhary."

pattern= re.compile("A random string.")
result= pattern.search(text)
print(result)

text2= "random string. nirmai003krm@gmail.com. some more random text.my name is rohitasw choudhary. cgh,jk.hlegdbj/o cl.aeb.kgdv/ich.kj,ā"
pattern= re.compile("[a-z0-9]+@[a-z0-9]+\.[a-z]+")
result= pattern.search(text2)
print(result)

print()
print()
print()

# Metacharacters
# Metacharacters are characters with a special meaning:


txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)

txt = "hello world"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)
print()

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
print()

x = re.findall("world$", txt)
if x:
  print("Yes, the string ends with 'world'")
else:
  print("No match")
print()

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 0 or more "x" characters:

x = re.findall("aix*", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()
print()

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 1 or more "x" characters:

x = re.findall("aix+", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "a" followed by exactly two "l" characters:

x = re.findall("al{2}", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

print()
print()

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()
print()

# Special Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

txt = "The rain in Spain"

#Check if the string starts with "The":

x = re.findall("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")
print()
print()
#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()





