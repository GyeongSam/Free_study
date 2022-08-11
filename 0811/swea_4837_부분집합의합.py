L=range(1,13)
for tc in range(1,int(input())+1):
    N,K=map(int,input().split())
    cnt=0   #갯수
    for i in range(1<<12):
        L_part=[]
        for j in range(12):
            if i & (1<<j):
                L_part.append(L[j]) #여기까지 부분집합 만들기
        if len(L_part)==N:  #len부터 판단
            SUM=0   #길이가맞다면 합 판단
            for x in L_part:SUM+=x
            if SUM ==K:cnt+=1   #맞다면 개수 증가
    print(f'#{tc} {cnt}')