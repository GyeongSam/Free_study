

def turn(n,d):
    pt[n][0]=(pt[n][0]-d+8)%8
    if n==1:pt[1][2]=(pt[1][2]-d+8)%8
    elif n==4:pt[4][1]=(pt[4][1]-d+8)%8
    else: pt[n][1]=(pt[n][1]-d+8)%8;pt[n][2]=(pt[n][2]-d+8)%8

def check(n):
    if (ws[n][pt[n][2]]!=ws[n+1][pt[n+1][1]]):return 1
    return 0

for t in range(1,int(input())+1):
    K=int(input())
    ws=[0]+[list(map(int,input().split())) for _ in '_'*4]

    pt=[0,[0,-1,2],[0,6,2],[0,6,2],[0,6,-1]]

    for _ in '_'*K:
        n,d=map(int,input().split())
        if n==1:
            if check(1):
                if check(2):
                    if check(3):
                        turn(4,-d)
                    turn(3,d)
                turn(2,-d)
            turn(1,d)
        elif n==2:
            if check(1):
                turn(1,-d)
            if check(2):
                if check(3):
                    turn(4,d)
                turn(3,-d)
            turn(2,d)
        elif n==3:
            if check(3):
                turn(4,-d)
            if check(2):
                if check(1):
                    turn(1,d)
                turn(2,-d)
            turn(3,d)
        elif n==4:
            if check(3):
                if check(2):
                    if check(1):
                        turn(1,-d)
                    turn(2,d)
                turn(3,-d)
            turn(4,d)
    ans=0
    for i in range(1,5):
        if ws[i][pt[i][0]]:ans+=2**(i-1)
    print(f'#{t}',ans)
