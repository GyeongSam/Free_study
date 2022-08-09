for T in range(1,11):
    N=int(input())
    L=[0,0]+list(map(int, input().split()))+[0,0]
    cnt=0
    for i in range(2,N+2):
        max=0
        for j in [-2,-1,1,2]:
            if L[i+j]>max:max=L[i+j]
        if L[i]>max:cnt+=L[i]-max

    print(f'#{T} {cnt}')


        