T=int(input())
for tc in range(T):
    N=int(input()) 
    L=list(map(int,input().split()))
    cnt=1
    cnt_max=0
    for i in range(1,N):
        cnt=cnt+1 if L[i-1]<L[i] else 1
        if cnt>cnt_max:cnt_max=cnt
    print(f'#{tc+1} {cnt_max}')
