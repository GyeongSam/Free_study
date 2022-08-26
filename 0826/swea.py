for T in range(1,int(input())+1):
    N,M=map(int,input().split())
    a,c=divmod(map(int,input().split()))
    b=a+1
    print(f'#{T}',a**(M-c)*b**c)
