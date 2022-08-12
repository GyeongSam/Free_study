for T in range(1,int(input())+1):
    N=int(input())
    L=list(map(int,input().split()))
    c=0
    while N>1:
        for i in range(N-1):
            if L[i]>L[i+1]:
                L[i],L[i+1]=L[i+1],L[i]
                c+=1
        N-=1
    print(f'#{T} {c}')
