def take(L,i,n,cnt=0):
    l=r=i
    d=1
    for _ in range(n):
        print(l,r)
        while l>=1 or r<=N:
            if l>=1 and L[l]==0:t=1;break
            if r<=N and L[r]==0:t=0;break
            else:
                l-=1
                r+=1
                d+=1
        if t: L[l]=1
        else: L[r]=1
        cnt+=d
    if t and r<=N and L[r]==0:
        sub=L[::]
        sub[r],sub[l]=sub[l],sub[r]
        return [L,sub],cnt
    return [L],cnt

N=9
print(take([1,0,0,0,0,0,0,0,3,0],3,4))