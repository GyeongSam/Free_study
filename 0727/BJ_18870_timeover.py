import sys

N=int(input())
L=list(sys.stdin.readline().split())
L_zip=[0]*N
cnt=0
for i in sorted(set(L)):
    L_index=[idx for idx,value in enumerate(L) if value==i]
    for num in L_index:
        L_zip[num]=cnt
    cnt+=1
print(' '.join(list(map(str, L_zip))))
