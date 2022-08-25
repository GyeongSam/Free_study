R=range(100)
for T in range(1,11):
    z=input()
    L=[list(map(int,input().split())) for _ in R]
    #1아래로 2위로
    cnt=0
    sub=0
    for j in R:
        for i in R:
            l=L[i][j]
            if l==1:sub=1
            elif l==2 and sub==1:cnt+=1;sub=0
    print(f'{T}',cnt)


