N,V=map(int,input().split())
L=[int(input()) for _ in '_'*N]
cnt=0
for c in L[::-1]:
    C,V=divmod(V,c)
    cnt+=C
print(cnt)
