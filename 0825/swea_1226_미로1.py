dx=[-1,1,0,0]
dy=[0,0,-1,1]
R=[0,1,2,3]
def go(x,y):
    S[x][y]=1             
    for i in R:         
        if(S[x+dx[i]][y+dy[i]]==0):
            next_R.append([x+dx[i],y+dy[i]])

for T in range(1,11):
    a=input()
    S=[[int(j) for j in list(input())] for _ in '_'*16]
    
    next_R=[[1,1]]
    goal=0

    while next_R and goal==0:
        x,y=next_R.pop()
        for i in R:
            if S[x+dx[i]][y+dy[i]]==3:goal=1
        go(x,y)
    print(f'#{T}',goal)
