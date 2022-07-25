COMBI_T=[]
COMBI=[[2]]
for N in range(3,12):
    sub=[]
    for i in COMBI:
        sub+=[[N]+i]
        for j in range(len(i)):
            sub+=[i[:j+1]+[N]+i[j+1:]]
    COMBI=sub
    if (N>=6):
        COMBI_T.append(COMBI)

TT=int(input())
for test_case in range(1,1+TT):
    N=int(input())
    A=list(map(int, input().split()))
    x=[]
    y=[]
    for i in range(len(A)):
        if (i%2==0):
            x.append(A[i])
        elif (i%2==1):
            y.append(A[i])

    def dis(a,b):
        return abs(x[a]-x[b])+abs(y[a]-y[b])

    
    COMB_d=[]
    sum=0
    for i in COMBI_T[N-5]:
        sum+=dis(0,i[0])
        for j in range(len(i)):
            if (j==len(i)-1):
                sum+=dis(i[j],1)
            else :
                sum+=dis(i[j],i[j+1])
        COMB_d.append(sum)
        sum=0

    print("#{}".format(test_case),min(COMB_d))
