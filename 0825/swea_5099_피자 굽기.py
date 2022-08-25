I=lambda :map(int,input().split())
for T in range(1,int(input())+1):
    N,M=I()
    P=list(I())
    Q=[x for x in range(N)]
    Pi=[x for x in range(N,M)]

    while len(Q)>1:
        P[Q[0]]=P[Q[0]]//2
        if P[Q[0]]!=0:
            Q.append(Q.pop(0))
        else:
            Q.pop(0)
            if Pi:Q.append(Pi.pop(0))
        print(Q,P)


    # while True:
    #     for l in Q:P[l]=P[l]//2
    #     i=0
    #     while i<len(Q):
    #         if P[Q[i]]==0:
    #             if Pi:Q[i]=Pi.pop(0)
    #             else:Q.pop(i);continue
    #         i+=1
    #     print(Q,Pi,P)
    #     if not Q:break    






        



    # Pi=[i for i in range(M)]
    # R=range(N)
    # Q=[]
    # while True:
    #     while len(Q)<N and Pi:
    #         Q.append(Pi.pop(0))
    #     for i in Q:
    #         P[i]=P[i]//2
    #     for l in Q:
    #         if not P[i]:Q.pop(i)
    #     if len(Q)==1:break
    #     print('Q:',Q)
    #     print('Pi:',Pi)
    #     print('P:',P)
    


    # for _ in R:Q.append(P.pop(0))
    # while True:
    #     for i in R:
    #         Q[i]=Q[i]//2
    #         if not Q[i]:
    #             Q.pop(i)
    #             if P:Q.append(P.pop(0))
    #     if len(Q)==1:break
