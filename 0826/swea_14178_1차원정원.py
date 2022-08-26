for T in range(1,int(input())+1):
    N,D=map(int,input().split())
    D=D*2+1
    print(f'#{T}',-(-N//D))