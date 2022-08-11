for T in range(1,int(input())+1):
    R=range(int(input()))
    L=[list(map(int,input().split()))for _ in R]
    P=[[0]*10 for _ in range(10)]
    cnt=0
    for l in L:
        for i in range(l[0],l[2]+1):
            for j in range(l[1],l[3]+1):
                if P[i][j] ==0:
                    P[i][j]=1
                    cnt+=1
    print(f'#{T} {cnt}')



