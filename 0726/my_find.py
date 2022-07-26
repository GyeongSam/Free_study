def my_find(text, alphabet):
    L=[]
    a=0
    while True:
        a=(' '*(a)+text[a:]).find(alphabet)
        if a==-1:
            break
        L.append(a)
        a+=1
    if L==[]:
        return -1
    else:
        return L

print(my_find('apple', 'p'))
print(my_find('a', 'p'))