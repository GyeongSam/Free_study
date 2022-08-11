
for tc in range(1, int(input())+1):
    N = int(input())
    R = [list(map(int, input().split())) for _ in range(N)]
    P = [[0]*10 for _ in range(10)]#도화지
    cnt=0   #칠한 횟수
    for ret in R:
        for i in range(ret[0],ret[2]+1):#i순회
            for j in range(ret[1],ret[3]+1):#j순회
                P[i][j]+=ret[4]#칠해요
                if P[i][j]>=3:#1,2가 같이칠해지면
                    cnt+=1#더해요
    print(f'#{tc} {cnt}')



