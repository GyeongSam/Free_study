from queue import PriorityQueue

for t in range(1,int(input())+1):
    N=int(input())
    L=[list(map(int,input().split())) for _ in '_'*N]
    V=[[1e10]*N for _ in '_'*N]
    V[0][0]=L[0][0]
    visit=[[0]*N for _ in '_'*N]
    visit[i][j]=1
    Q=PriorityQueue()
    Q.put((1,(0,0)))

    while(Q):
        now=Q.get()
        i=now[1][0]
        j=now[1][1]
        for di,dj in [(1,0),(0,1)]:
            I,J=now[1][0]+di,now[1][1]+dj
            if I<N and J<N and V[I][J]>V[i][j]+L[I][J] and not visit[I][J]:
                V[I][J]=V[i][j]+L[I][J]
                visit[I][J]=1
                Q.put((L[I][J],(I,J)))

    print(f'#{t}',V[N-1][N-1])