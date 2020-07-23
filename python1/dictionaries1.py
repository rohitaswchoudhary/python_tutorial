contacts={'rohit':{'phone':'7091741989','email':'rohitaswchoudhary@gmail.com'},
'mom':{'phone':'8051156856','email':'archanachoudharyjsr@gmail.com'},
'bigb':{'phone':'9771416543','email':'jagritijani998@gmail.com'}
}
 

print(contacts.get('rohit'))
print(contacts.get('bigb'))
print(contacts.get('mom'))

contacts['rohitasw']={'phone':'9123275996','email':'rohitaswchoudhary@hotmail.com'}
print(contacts)


sentence= 'I like the name Rohit because the name Rohit is the best.'

word_count={

            'the':3,
            'I':1,
            'like':1

}
#dict.items()

print(list(word_count.items()))

#dict.keys()
print(word_count.keys())

#dict.values
print(word_count.values())

# pop items from dict:
#dict.pop(key)

'''
pop=word_count.pop('I')
print(pop)
print(word_count)
'''

#dict.popitem()
#pop the last added item

popitem=word_count.popitem()
print(popitem)
print(word_count)

word_count['Rohit']=2
print(word_count)

word_count.clear()
print(word_count)

print("!!------------------------------------\\\\\\\\\---------------------------------------------------!!")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# accessing items.
x = thisdict["model"]

print()
x = thisdict.get("model")
print(x)
# change value.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2020
print(thisdict)

# looping through  DICTIONARIES.
for x in thisdict:
  print(x)


for x in thisdict:
  print(thisdict[x])

# check if key exists.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# length
print(len(thisdict))

# EDITING DICT.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

print()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

print()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# copy a dict.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# nested dict.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

