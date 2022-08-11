R=range(100)
for tc in range(1,11):
    X=input()
    L=[list(map(int,input().split())) for _ in R]
    MAX=0
    sum3,sum4=0,0
    for n in R:
        sum1,sum2=0,0
        for l in R:
            sum1+=L[n-l][n]
            sum2+=L[n][n-l]
        sum3+=L[n][n]
        sum4+=L[99-n][n]
        if sum1>MAX:MAX=sum1
        if sum2>MAX:MAX=sum2
    if sum3>MAX:MAX=sum3
    if sum4>MAX:MAX=sum4
    print(f'#{tc} {MAX}')
 