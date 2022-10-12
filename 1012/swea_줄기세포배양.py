import pprint
for t in range(1,int(input())+1):
    N,M,K=map(int,input().split())
    L=[[0]*(400+M) for _ in '_'*200]+[[0]*200+list(map(int,input().split()))+[0]*200 for _ in '_'*N]+[[0]*(400+M) for _ in '_'*200]
    Q=[]
    ql=0;qr=0
    for i in range(200,200+N):
        for j in range(200,200+M):
            if L[i][j]:
                Q.append((i,j));qr+=1
                temp=L[i][j]
                L[i][j]=[temp,temp+1,0]
    T=0
    while(ql<qr):
        i,j=Q[ql];ql+=1
        # print(i,j,L[i][j][0],L[i][j][1],L[i][j][2])
        if L[i][j][2]>=K: break
        # if L[i][j][2]==T:T+=1;print(Q[ql-1:qr])


        c=L[i][j][0]
        gt=L[i][j][1]
        L[i][j][2]+=1
        nt=L[i][j][2]
        if gt==nt:
            for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni,nj=i+di,j+dj
                if L[ni][nj]==0:
                    Q.append((ni,nj));qr+=1
                    L[ni][nj]=[c,nt+c+1,nt]
                elif L[ni][nj] and L[ni][nj][1]-1-L[ni][nj][0]==nt and L[ni][nj][0]<c:
                    L[ni][nj]=[c,nt+c+1,nt]

        if L[i][j][1]+c-1<=L[i][j][2]:
            L[i][j]=[]
        else: Q.append((i,j));qr+=1


    cnt=0
    for i in range(400+N):
        for j in range(400+M):
            if L[i][j]:cnt+=1
    print(f'#{t}',cnt)




