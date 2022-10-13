import pprint

I=lambda :map(int,input().split())

di=[0,-1,0,1,0]
dj=[0,0,1,0,-1]

for t in range(1,int(input())+1):
    M,A=I()
    movingA=list(I())
    movingB=list(I())
    APs=[list(I()) for _ in '_'*A]
    APs.sort(key=lambda x:-x[3])
    field=[[[] for _ in '_'*11] for _ in '_'*11]
    x=-1
    for AP in APs:
        x+=1
        ny,nx=AP[0],AP[1]
        R=range(-AP[2],AP[2]+1)
        for dy in R:
            for dx in R:
                tx,ty=nx+dx,ny+dy
                if tx<1 or tx>10 or ty<1 or ty>10 or abs(dx)+abs(dy)>AP[2]:continue
                field[tx][ty].append(x)
    A=[1,1]
    B=[10,10]
    ans=0


    for time in range(M+1):
        canA=field[A[0]][A[1]];la=len(canA)
        canB=field[B[0]][B[1]];lb=len(canB)
        if time!=M:
            A[0]+=di[movingA[time]]
            A[1]+=dj[movingA[time]]
            B[0] += di[movingB[time]]
            B[1] += dj[movingB[time]]

        if la==0 and lb==0:continue
        elif la==0 and lb!=0:ans+=APs[canB[0]][3]
        elif (la != 0 and lb == 0) or (la==lb==1 and canA[0]==canB[0]): ans += APs[canA[0]][3]
        elif canA[0]==canB[0]:
            if la>1 and lb>1:
                if canA[1]<canB[1]:ans+=APs[canA[1]][3]+APs[canB[0]][3]
                else:ans+=APs[canA[0]][3]+APs[canB[1]][3]
            elif la>1:
                ans+= APs[canA[1]][3] + APs[canB[0]][3]
            elif lb>1:
                ans += APs[canA[0]][3] + APs[canB[1]][3]
        else:ans+=APs[canB[0]][3]+APs[canA[0]][3]
    print(f'#{t}',ans)

