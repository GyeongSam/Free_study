i=int;I=input
for T in range(1,i(I())+1):
    N,M=I().split()
    L=list(I().split())
    C=i(M)%i(N)
    for _ in '_'*C:L.append(L.pop(0))
    print(f'#{T}',L[0])