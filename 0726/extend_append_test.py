a=['a', 'b', 'c']
b='de'
c=['d','e'] 
a.append(b)     
print(a)        #['a', 'b', 'c', 'de']

a=['a', 'b', 'c']
a.append(c)
print(a)        #['a', 'b', 'c', 'de']

a=['a', 'b', 'c']
a.extend(b)
print(a)        #['a', 'b', 'c', 'd', 'e']

a=['a', 'b', 'c']
a.extend(c)
print(a)        #['a', 'b', 'c', 'd', 'e']
