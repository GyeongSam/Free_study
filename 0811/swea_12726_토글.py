I=lambda:map(int,input().split())
for T in range(1,int(input())+1):
    N,M=I();R=range(N);L=[list(I())for _ in R]
    for k in range(1,M+1):
        for i in R:
            for j in R:
                if not M%k:L[i][j]=1-L[i][j]
                elif not (i+j+2)%k:L[i][j]=1-L[i][j]
    cnt=0
    for x in L:
        for y in x:
            if y==1:cnt+=1
    print(f'#{T} {cnt}')




