T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    height_list=list(map(int,input().split()))+[0]  #편의를위해 높이 리스트에 0을 하나 추가해줍니다
    before_h=0                          #이 전 높이를 저장할 변수입니다.
    cnt=0                               #봉우리 개수를 카운트할 변수입니다.
    increase=0                          #1이면 증가하던 상태고 0이면 감소하던 상태입니다

    for h in height_list:               #높이 리스트를 돌면서
        if h>before_h:                  #이 전보다 크다면 증가상태 표시합니다.
            increase=1
        elif h<before_h and increase:   #이 전보다 작아졌는데 증가상태였다면
            cnt+=1                      #봉우리를 하나 카운트 해주고
            increase=0                  #감소상태로 만듭니다
        before_h=h                      #이번 봉우리 높이를 저장합니다
    print(f'#{test_case}',cnt)          