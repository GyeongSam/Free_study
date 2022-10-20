
for t in range(1,1+int(input())):
    N=int(input())
    b=0
    ans=0
    n_list=list(map(int,input().split())) #리스트로 저장
    b=n_list[-1] #리스트이 마지막 값을 넣고
    for value in n_list[::-1]:  #앞의 값과 비교
        if value > b:
            b = value
        else:
            ans+=b-value
    print(f'#{t}',ans)