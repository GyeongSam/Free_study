
def BT(value,costs,last_choice):    #현재까지 가치,보석 가치 목록,마지막 고른 보석을 인자로받습니다.
    global MAX                      #최대가치를 갱신할 글로벌 변수입니다.
    global M                        #예산을 넘지않기위한 글로벌 변수입니다.
    for i in range(last_choice+1,len(costs)):   #마지막으로 선택한 인덱스 바로 뒤부터 끝까지 순회합니다.
        if (value+costs[i])>M:      #만약 이번 보석을 더하는 것이 예산 초과가 된다면
            if value>MAX:MAX=value  #현재 가치가 최대값인지 확인하고 맞다면 갱신해줍니다
            return                  #더이상 진행은 무의미하므로 돌아갑니다.
        else:                       #아니라면
            BT(value+costs[i],costs,i)      #현재 가치를 더하고 다음 선택으로 넘어갑니다

T=int(input())
for test_case in range(1,T+1):          
    N,M=map(int,input().split())
    costs=list(map(int,input().split()))
    valid_costs=[]          #수집 대상인 보석들만 저장하기 위한 공간입니다.
    MAX=0
    for cost in costs:          #각 보석을 돌면서
        for n in [4,6,7,9,11]:  #수집대상 보석인지
            if (cost%n)==0:                 #확인하고
                valid_costs.append(cost)        #맞다면 추가합니다.
                break
    valid_costs.sort()  #빽트래킹을 간단하게 하기위해 오름차순 정렬합니다.
    BT(0,valid_costs,-1)    # (0의 가치,보석가치목록,인덱스0부터선택가능)을 인자로 호출합니다.

    print(f'#{test_case}',MAX)