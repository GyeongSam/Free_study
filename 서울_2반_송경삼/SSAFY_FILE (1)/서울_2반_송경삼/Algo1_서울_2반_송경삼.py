di=[1,0,-1,0]
dj=[0,1,0,-1]
T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    ans=0                                           #정답을 카운트할 변수입니다.
    feild=[list(map(int,input().split())) for _ in '_'*N]   #인풋을 받을 2차원리스트입니다.
    for i in range(N):          
        for j in range(N):      #2차원 리스트를 돌면서  
            if feild[i][j]==2:          #만약 타워를 만났다면
                for d in range(4):              #타워의 네방향을 각자볼 것입니다.
                    ni,nj=i+di[d],j+dj[d]           #각 방향에서
                    while(0<=ni<N and 0<=nj<N and (feild[ni][nj]==0 or feild[ni][nj]==3)):
                        feild[ni][nj]=3         #범위를 벗어나지 않고, 벽과 타워가 아닌 지역을 공격처리(3으로 표시)합니다.
                        ni+=di[d]               #공격할 수 있을 때 까지 다음 칸으로 넘어가 반복합니다. 
                        nj+=dj[d]
    for i in range(N):
        for j in range(N):          #공격 처리한 땅을 돌면서
            if feild[i][j]==0:      #만약 공격받지 않은 땅이 있다면
                ans+=1              #카운트 해줍니다.
    print(f'#{test_case}',ans)






