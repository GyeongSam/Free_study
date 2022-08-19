A=[1,2,3]
B=['a','b','c']

for x,y in zip(*(A,B)):
    print(x,y)