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



