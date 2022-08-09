for T in range(int(input())):
    N=int(input())
    l=list(map(int,input()))
    C=[0]*10
    ans=[0,0]
    for i in l:
        C[i]+=1
    for j in range(10):
        if C[j]>=ans[1]:
            ans[0]=j
            ans[1]=C[j]
    print(f'#{T+1} {ans[0]} {ans[1]}')
