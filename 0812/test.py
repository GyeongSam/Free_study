D={'ZRO':0,'ONE':1,'TWO':2,'THR':3,'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
for t in range(int(input())):
    T,M=input().split()
    L=list(input().split())
    ans=[0]*10
    for i in L:
        ans[D[i]]+=1
    print(T)
    n=[]
    for k,v in D.items():n+=[k]*ans[v]
    print(*n)

