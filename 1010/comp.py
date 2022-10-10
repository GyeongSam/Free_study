di=[0,1,0,-1]
dj=[1,0,-1,0]
R4=range(4)
 
def dfs(i,j,h,k,cnt):
    global ans,K
    global height,visited
    if cnt>ans:ans=cnt
    for d in R4:
        ni,nj=i+di[d],j+dj[d]
        if not (ni<0 or ni>=N or nj<0 or nj>=N):print(f'ni:{ni},nj:{nj},v?:{visited[ni][nj]}')

        if ni<0 or ni>=N or nj<0 or nj>=N or visited[ni][nj]:continue
        if h>height[ni][nj]:
            visited[ni][nj]=1
            dfs(ni,nj,height[ni][nj],k,cnt+1)
            visited[ni][nj]=0
        if not k:
            for dk in range(1,K+1):
                if h>height[ni][nj]-dk:
                    visited[ni][nj]=1
                    dfs(ni,nj,height[ni][nj]-dk,dk,cnt+1) 
                    visited[ni][nj]=0
 
for t in range(1,int(input())+1):
    N,K=map(int,input().split())
    height=[list(map(int,input().split())) for _ in '_'*N]
    visited=[[0]*N for _ in '_'*N]
    R=range(N)
    max_height=0
    ans=0
    for i in R:
        for j in R:
            if height[i][j]>max_height:
                max_height=height[i][j]
    for i in R:
        for j in R:
            if height[i][j]==max_height:
                visited[i][j]=1
                dfs(i,j,max_height,0,1)
                visited[i][j]=0
    print(f'#{t}',ans)