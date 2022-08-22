def check(D):
    if D==0 and Room[I][J+1]!=1:
            return 1
    elif D==2 and Room[I+1][J]!=1:
            return 1
    else:
        for di,dj in (0,1),(1,1),(1,0):
            if Room[I+di][J+dj]==1:
                break
        else:return 1
    return 0

def isN(di,dj):
    if I+di==N and J+dj==N:
        return 1
    return 0

N=int(input())
Room=[[1]*(N+2)]+[[1]+list(map(int,input().split()))+[1] for _ in '_'*N]+[[1]*(N+2)]
stack=[(1,2,0)]
cnt=0
while stack!=[]:
    I,J,d=stack.pop()
    if check(1):
        if isN(1,1):cnt+=1
        else:stack.append((I+1,J+1,1))
    if d!=2 and check(0):
        if isN(0,1):cnt+=1
        else:stack.append((I,J+1,0))
    if d!=0 and check(2):
        if isN(1,0):cnt+=1
        else:stack.append((I+1,J,2))
print(cnt)



