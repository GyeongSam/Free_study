N=int(input())
Room=[[1]*(N+2)]+[[1]+list(map(int,input().split()))+[1] for _ in '_'*N]+[[1]*(N+2)]
stack=[(1,2,0)]
cnt=0
while stack!=[]:
    I,J,d=stack.pop()
    if I+1==N or J+1==N


        stack.append((I+1,J+1,1))
    if d!=2 and check(0):
        if isN(0,1):cnt+=1
        else:stack.append((I,J+1,0))
    if d!=0 and check(2):
        if isN(1,0):cnt+=1
        else:stack.append((I+1,J,2))
print(cnt)