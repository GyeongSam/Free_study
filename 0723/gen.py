N=int(input())

def m_l(L,N_par):
    l1=[]
    l2=[]
    for x in L:
        if x[1]==2:
            l1.append([x[0],3])
            l2.append([x[0],1])
        elif x[1]==3:
            l1.append([x[0],2])
            l2.append(x)
        elif x[1]==1:
            l1.append(x)
            l2.append([x[0],2])
    if N_par==max([i[0] for i in L])+1:
        return l1+[[max([i[0] for i in L])+1,3]]+l2
    else:
        return m_l(l1+[[max([i[0] for i in L])+1,3]]+l2,N_par)

X=m_l([[1,3]],N)
print(len(X))
for i in X:
    print(i[0],i[1])

