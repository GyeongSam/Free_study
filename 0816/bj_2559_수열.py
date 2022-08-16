def S(n):
    return A[n-1]-L[n-1]+L[n+M-1]
I=lambda :map(int,input().split())
N,M=I()
L=list(I())
A=[sum([L[i] for i in range(M)])]
m=A[0]
for i in range(1,N-M+1):
    sub=S(i)
    if sub>m:m=sub
    A.append(sub)
print(A)
print(m)
