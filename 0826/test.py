def com(L,n):
    ll = len(L[0])
    SUB=[]
    for P in L:
        for l in range(ll + 1):
            for r in range(l, ll + 1):
                sub=P[:]
                sub[r:r]=[-n]
                sub[l:l]=[n]
                SUB.append(sub)
    return SUB
print(com([[1,-1]],2))
