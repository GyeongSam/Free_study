di=[1,0,-1,0]
dj=[0,1,0,-1]
N=int(input())
R=range(N)
L=[];Q=[]
visit=[[0]*N for _ in R]
for i in R:L.append(input())
is_neer=is_RG=cnt1=cnt2=0


def bfs(c):
    global is_neer,is_RG

    while(Q):

        A=Q.pop(0)

        for d in range(4):

            B=(A[0]+di[d],A[1]+dj[d])
            if B[0]<0 or B[0]>=N or B[1]<0 or B[1]>=N:continue

            if is_RG and visit[B[0]][B[1]] and L[B[0]][B[1]]!='B' and L[B[0]][B[1]]!=c:
                is_neer=1
                is_Rg=0
                #순회중에 이미 방문했으면서 초록 <-> 빨강이 근처에 붙어있다면 is_neer=True

            if not visit[B[0]][B[1]] and L[B[0]][B[1]]==c:
                visit[B[0]][B[1]]=1
                Q.append(B)
                #같은색깔인 곳들 다 방문처리


for i in R:
    for j in R:
        if not visit[i][j]:
            
            is_neer=0
            is_RG=1 if L[i][j]!='B' else 0 #초or빨이면 is_RG=True

            Q.append((i,j))
            visit[i][j]=1
            bfs(L[i][j])    #방문하지않은 곳을 방문처리하고 bfs함수 호출

            cnt1+=1     #호출됐으니 정상인은 카운트+1
            if is_neer:neer=0   #초<->빨 근접이라면 적록색약은 카운트X
            else: cnt2+=1       #안붙어있다면 적록색약도 카운트

print(cnt1,cnt2)