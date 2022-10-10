
di=[0,1,0,-1]
dj=[1,0,-1,0]
R4=range(4)

def dfs(i,j,v,h,k,cnt):
    global ans
    if cnt>ans:ans=cnt
    for d in R4:
        ni,nj=i+di[d],j+dj[d]
        if not (ni<0 or ni>=N or nj<0 or nj>=N):print(f'ni:{ni},nj:{nj},v?:{v&1<<(N*ni+nj)}')
        if ni<0 or ni>=N or nj<0 or nj>=N or (v&1<<(N*ni+nj)):continue
        if h>height[ni][nj]:
            dfs(ni,nj,v|(1<<(N*i+j)),height[ni][nj],k,cnt+1)
        if not k:
            for dk in RK:
                if h>height[ni][nj]-dk:
                    dfs(ni,nj,v|(1<<(N*i+j)),height[ni][nj]-dk,dk,cnt+1) 

for t in range(1,int(input())+1):
    N,K=map(int,input().split())
    height=[list(map(int,input().split())) for _ in '_'*N]
    visited=[[0]*N for _ in '_'*N]
    R=range(N)
    RK=range(1,K+1)
    max_height=0
    ans=0
    for i in R:
        for j in R:
            if height[i][j]>max_height:
                max_height=height[i][j]
    for i in R:
        for j in R:
            if height[i][j]==max_height:
                dfs(i,j,(1<<(N*i+j)),max_height,0,1)
    print(f'#{t}',ans)



