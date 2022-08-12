L=[]
for _ in range(int(input())):
    axis,height=map(int,input().split())
    if len(L)<axis:#이번요소가 axis에 없다면
        L+=[0]*(axis-len(L))+[height] #0과 본인의 행렬을 같읻
    else: L[axis]=height
    L+=[0,0]
r=len(L)-1
M=max(L)
l,l_m,r_m=(0,)*3
while L[l]!=M:
    if L[l]>l_m:l_m=L[l]
    else:L[l]=l_m
    l+=1
while L[r]!=M:
    if L[r]>r_m:r_m=L[r]
    else:L[r]=r_m
    r-=1
if l<r:
    for i in range(l,r+1):
        L[i]=M
print(sum(L))
