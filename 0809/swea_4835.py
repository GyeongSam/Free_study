def sum_L(I):   # L 리스트의 M구간만큼 합을 리턴하는 함수입니다.
    sum=0
    for n in range(M):
        sum+=L[I+n]
    return sum

for tc in range(int(input())):  
    N,M=map(int,input().split())    
    L=list(map(int,input().split()))
    max,min=sum_L(0),sum_L(0) #초항 설정합니다.
    for i in range(1,N-M+1):    #1부터 N-M까지 순회합니다.
        if sum_L(i)>max:max=sum_L(i)    #최대 갱신
        if sum_L(i)<min:min=sum_L(i)    #최소 갱신
    print(f'#{tc+1} {max-min}')     #정답 출력합니다.
