for t in range(1,int(input())+1):
    N=float(input())
    a=str()
    for i in range(1,13):
        if N>=2**-i:
            N-=2**-i
            a+='1'
        else: a+='0'
        if N==0:break
    else:a='overflow'
    print(f'#{t}',a)

