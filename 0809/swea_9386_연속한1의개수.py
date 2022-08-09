T=int(input())
for tc in range(T):
    N=int(input()) 
    L=list(map(int,input()))
    cnt=0
    cnt_max=0
    for i in L:
        cnt=cnt+1 if i==1 else 0
        if cnt>cnt_max:cnt_max=cnt
    print(f'#{tc+1} {cnt_max}')      