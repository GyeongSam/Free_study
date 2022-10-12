di=[1,0,-1,0]
dj=[0,1,0,-1]
R4=range(4)

def cn(i,j,d):
    ti,tj=i+di[d],j+dj[d]
    while(0<=ti<N and 0<=tj<N and field[ti][tj]==0):ti+=di[d];tj+=dj[d]
    if not (ti==-1 or ti==N or tj==-1 or tj==N): return 0
    ti,tj=i+di[d],j+dj[d];cnt=0
    while(0<=ti<N and 0<=tj<N):field[ti][tj]=1;cnt+=1;ti+=di[d];tj+=dj[d]
    return cnt

def dcn(i,j,d):
    ti,tj=i+di[d],j+dj[d]
    while(0<=ti<N and 0<=tj<N):field[ti][tj]=0;ti+=di[d];tj+=dj[d]

def dfs(n,v,s):
    print(bin(v))
    global ans
    if n>l:return
    if n>ans[0]: ans=[n,s]
    elif n==ans[0] and s<ans[1]: ans[1]=s
    for x in Rl:
        if v&(1<<x):continue
        
        i,j=cells[x]
        for d in R4:
            temp=cn(i,j,d)
            if temp:
                dfs(n+1,v|(1<<x),s+temp)
                dcn(i,j,d)


for t in range(1,int(input())+1):
    N=int(input());R=range(1,N-1)
    field=[list(map(int,input().split())) for _ in '_'*N]
    ans=[0,1<<10]
    cells=[]
    for i in R:
        for j in R:
            if field[i][j]:cells.append((i,j))
    l=len(cells);Rl=range(l)
    dfs(0,0,0)
    # cells.sort(key=lambda x:(min(x[0],N-x[0])+min(x[1],N-x[1])))
    print(f'#{t}',ans[1])

