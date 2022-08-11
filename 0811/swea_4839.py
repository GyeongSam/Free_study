def BS(L, key):
    start=0
    end=len(L)-1
    cnt=0
    while start<=end:
        cnt+=1
        mid=int((start+end)/2)
        if L[mid]==key:
            return cnt
        elif L[mid]>key:
            end=mid
        else:
            start=mid
    return -1

for tc in range(1,int(input())+1):
    N,k1,k2 = map(int,input().split())
    L=range(1,N+1)
    A,B=BS(L,k1),BS(L,k2)
    if A<B:win='A'
    elif B<A:win='B'
    else:win=0
    print(f'#{tc} {win}')





