import heapq
for t in range(1,int(input())+1):
    N,E=map(int,input().split())
    Edge=[[] for _ in '_'*(N+1)]
    DP=[0]+[1e10]*N
    for _ in '_'*E:
        s,e,w=map(int,input().split())
        Edge[s].append((e,w))
    HQ=[]
    heapq.heappush(HQ,(0,0))
    while(1):
        v,n=heapq.heappop(HQ)
        if n==N:break
        for e,w in Edge[n]:
            if DP[e]>v+w:
                DP[e]=v+w
                heapq.heappush(HQ,(DP[e],e))
    print(f'#{t}',DP[N])
