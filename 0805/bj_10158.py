w,h=map(int, input().split())
x,y=map(int, input().split())
t=int(input())
d=1
while True:
    if d==1:
        if (w-x)<(h-y):
            d=2
            if t>(w-x):
                t-=(w-x)
            else:
                print(x+t,y+t)
                break
            x=w
            y+=(w-x)
        else:
            d=4
            if t>(h-y):
                t-=(h-y)
            else:
                print(x+t,y+t)
                break
            x+=(h-y)
            y=h

    elif d==2:
        if x<(h-y):
            d=1
            if t>x:
                t-=x
            else:
                print(x-t,y+t)
                break
            x=0
            y+=x
        else:
            d=3
            if t>(h-y):
                t-=(h-y)
            else:
                print(x-t,y+t)
                break
            x-=(h-y)
            y=h

    elif d==3:
        if x<y:
            d=4
            if t>x:
                t-=x
            else:
                print(x-t,y-t)
                break
            x=0
            y-=x
        else:
            d=2
            if t>y:
                t-=y
            else:
                print(x-t,y-t)
                break
            x-=y
            y=0
    else:
        if (w-x)<y:
            d=3
            if t>(w-x):
                t-=(w-x)
            else:
                print(x+t,y-t)
                break
            x=w
            y-=(w-x)
        else:
            d=1
            if t>y:
                t-=y
            else:
                print(x+t,y-t)
                break
            x+=y
            y=0


