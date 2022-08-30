for T in range(1,int(input())+1):
    D,A,B,F=map(int,input().split())
    print(f'#{T}',D/(A+B)*F)