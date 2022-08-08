import sys
N=int(input())
L=list(map(int, sys.stdin.readline().split()))
sub=sorted(enumerate(L), key=lambda x:x[1])
ans=[0]*N
cnt=0
for v in range(1,N):
    if sub[v][1]>sub[v-1][1]:
        cnt+=1
    ans[sub[v][0]]=cnt
A=' '.join(map(str, ans))
print(A)
