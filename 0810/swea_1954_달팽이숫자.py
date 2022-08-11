cd=[1,2,3,0]    #방향 전환용
d=[(0,1),(1,0),(0,-1),(-1,0)]   #이동방향

for tc in range(1,int(input())+1):
    N=int(input())
    L=[[0]*N for _ in range(N)]
    check=[N-1,N-1,0,0] #마지막인지 체크용
    i,j=0,0 #항번호
    D=0 #방향 변수
    di,dj=d[D]  #이동방향
    for n in range(1,N**2+1):
        L[i][j]=n   #리스트 갱신
        if (D%2 and i==check[D]) or (not D%2 and j==check[D]) or L[i+di][j+dj]!=0:
            D=cd[D] #만약 끝에 도착or다음이 이미 방문
            di,dj=d[D]  #방향 바꿈
        i+=di   #좌표 갱신
        j+=dj
    print(f'#{tc}')
    for q in range(N):
        print(*L[q])

        
