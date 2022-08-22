for T in range(1,int(input())+1):
    A=input()
    B=input()
    D={}
    M=0
    for i in A:
        if i not in D:
            D[i]=0
    for j in B:
        if j in D:
            D[j]+=1
            if D[j]>M:M=D[j]

    print(f'#{T} {M}')


