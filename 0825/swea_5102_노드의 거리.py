def go(ls): #출발리스트를 받아 도착리스틀 반환하는 함수
    sub=[]
    for i in ls:
        sub+=[j for j,x in enumerate(p[i]) if x==1 and j not in V]
    return sub
I=lambda :map(int,input().split())
for T in range(1,int(input())+1):
    V,E=I()
    p=[[0]*(V+1) for _ in '_'*(V+1)]    #간선 여부 2차원 배열 초기값
    for _ in '_'*E:
        A,B=I()     #input으로 간선 갱신
        p[A][B]=1
        p[B][A]=1
    S,G=I()
    Q=[S]   #방문할 큐
    V={S}   #방문한 곳
    cnt=0   #이동 간선수
    while True:
        Q=go(Q) #이동
        V.update(Q) #방문한 곳 갱신
        cnt+=1
        if G in Q:break #도착했다면 종료
    print(f'#{T}',cnt)





