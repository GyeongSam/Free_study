def is_hansu(x):
    R=[int(i) for i in str(x)]
    if len(R)==1:
        return True 
    else:
        if len(set([R[x+1]-R[x] for x in range(len(R)-1)]))==1:
            return True
        else:
            return False

N=int(input())
cnt=0
for i in range(1,N+1):
    if is_hansu(i)==True:
        cnt+=1
print(cnt)
