import time
start=time.time()

for tc in range(int(input())):
    K,N,M=map(int,input().split()) 
    L=list(map(int,input().split()))
    cnt=0   #충전 횟수
    position=0  #현재 위치
    while True:
        sub=0   #이동 여부 판단용 보조 변수
        for i in range(position+K,position,-1): #현재 위치에서 이동가능위치만큼 역순회합니다
            if i in L:  #가장 멀리 갈 수있는 충전소가 있다면
                position=i  #위치갱신
                cnt+=1  #충전횟수 +1
                sub=1   #이동 했다 표시
                break   #멀리 이동했으니 for문 탈출
        if sub==0 or position+K>=N :
            break   #이동 못했거나 다음 이동거리가 도착점을 벗어난다면
    print(f'#{tc+1} {cnt if sub!=0 else 0}')    #출력 후 종료
print(time.time()-start)