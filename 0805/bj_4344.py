N=int(input())
for t in range(N):
    L=list(map(int, input().split()))
    cnt=0
    m=sum(L[1:])/L[0]
    for _ in L[1:]:
        if _>m:
            cnt+=1
    print('{:.3f}%'.format(round(cnt/L[0]*100)))
