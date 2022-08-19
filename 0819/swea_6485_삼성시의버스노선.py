for T in range(1,int(input())+1):
    N=int(input())
    bus=[0]*5001
    for _ in '_'*N:
        l,r=map(int,input().split())
        for i in range(l,r+1):
            bus[i]+=1
    P=int(input())
    ans=[bus[int(input())] for _ in '_'*P]
    print(*ans)
