for t in range(1,int(input())+1):
    N,W=input().split()
    a=str()
    for w in W:
        n=int(w,16)
        for i in range(3,-1,-1): a+='1' if ((1<<i)&n)==(1<<i) else '0'
    print(f'#{t}',a)
        


