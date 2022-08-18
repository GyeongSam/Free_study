I=lambda :map(int,input().split())
r=[0]*12
N,K=I()
for _ in '_'*N:
    s,g=I()
    if s:r[g+5]+=1
    else:r[g-1]+=1
cnt=0
for i in r:
    cnt+=i//K + (1 if i%K!=0 else 0) 
print(cnt)

