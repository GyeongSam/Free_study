X,Y=map(int, input().split())
N=int(input())
sub=0
if N>X*Y:
    print(0)
else:
    for i in range(1,N):
        if N-(Y-i)>0:
            N-=(Y-i)
            print(N)
        else:break
        if N-(X-i)>0:
            N-=(X-i)
            print(N)
        else:
            sub=1
            break
    
    if i%2 and sub==0:
        print(1+(i//2),(i//2)+N)
    elif i%2 and sub==1:
        print(1+(i//2)+N,Y-(i//2))
    elif not i%2 and sub==0:
        print(X-(i//2),Y-(i//2)-N)
    elif not i%2 and sub==1:
        print(X-(i//2)-N,1+(i//2))


