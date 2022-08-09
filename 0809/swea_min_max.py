for T in range(int(input())):   #테스트 케이스를 반복합니다.
    N=int(input())  #N을 받습니다
    M=0;m=1000000   #M,m의 초기값을 설정합니다.
    s=list(map(int,input().split()))    #리스트를 받고 저장합니다.
    for i in s: #각 요소를 순회하면서
        if i>M:M=i  #최대값 갱신
        if i<m:m=i  #최소값 갱신
    print(f'#{T+1} {M-m}')  #뺀값을 출력합니다.
    
