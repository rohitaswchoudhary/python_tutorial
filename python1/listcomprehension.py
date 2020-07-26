names= ['Neha','Aditi','Ritu','Susanj','Sophie']

l=[]
for person in names:
    l.append(person)
print(l)

print([person for person in names]) #listcomp....

l=[]
for person in names:
    l.append(person+" dumped me.")
print(l)

print([person+' dumped me.' for person in names])


movies_ratings={'Intestallar':9,'pk':10,'3idiots':10,'dark knight':7,'50 shades':2}
l=[]
for movie in movies_ratings:
    if movies_ratings[movie]>8:
        l.append(movie) 

print(l)

print([movie for movie in movies_ratings if movies_ratings[movie]>6])





