
X,Y=map(int, input().split())
N=int(input())

x,y=1,0
if N>X*Y:
    print(0)
else:
    for cnt in range(0,N,2):
        if N<=0:
            break
        if N-(Y-cnt)>=0:
            y+=Y-cnt
            N-=Y-cnt
        else:
            y+=N
            break 
        
        if N-(X-1-cnt)>=0:
            x+=(X-1-cnt)
            N-=(X-1-cnt)
        else:
            x+=N
            break
        
        if N-(Y-1-cnt)>=0:
            y-=(Y-1-cnt)
            N-=(Y-1-cnt)
        else:
            y-=N
            break 
        
        if N-(X-2-cnt)>=0:
            x-=(X-2-cnt)
            N-=(X-2-cnt)
        else:
            x-=N
            break
    
    
    print(x,y)


    

