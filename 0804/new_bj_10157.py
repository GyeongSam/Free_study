def move(N,X,Y):
    x,y=1,0
    for i in range(N):
        if i%4==0:
            if N>=Y-(i//4):
                y+=(Y-i//4)
                N-=(Y-i//4)
            else:
                y+=(N)
                return x,y
        
        if i%4==1:
            if N>X-1-i//4:
                x+=(X-1-i//4)
                N-=(X-1-i//4)
            else:
                x+=(N)
                return x,y
        
        if i%4==2:
            if N>=Y-1-i//4:
                y-=(Y-1-i//4)
                N-=(Y-1-i//4)
            else:
                y-=(N)
                return x,y
        
        if i%4==3:
            if N>=X-2-i//4:
                x-=(X-2-i//4)
                N-=(X-2-i//4)
            else:
                x-=(N)
                return x,y
            

            

            



X,Y=map(int, input().split())
N=int(input())

if N>X*Y:
    print(0)
else:
    print(move(N,X,Y))