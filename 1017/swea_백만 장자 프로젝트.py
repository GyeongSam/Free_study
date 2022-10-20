for t in range(1,1+int(input())):
    N=int(input())
    values=list(map(int,input().split()))
    max_value=values[-1]
    ans=0
    for value in values[::-1]:
        if value>max_value:max_value=value
        else:ans+=max_value-value
    print(f'#{t}',ans)
