for tc in range(1,int(input())+1):
    L=list(map(int,input().split()))
    n=len(L)
    ans=0
    for i in range(1<<n):
        L_part=[]
        for j in range(n):
            if i & (1<<j):
                L_part.append(L[j])
        if L_part!=[]:
            sum=L_part[0]
            for x in L_part:
                sum+=x
            if sum==0:
                ans=1
                break

    print(f'#{tc} {ans}')


        


