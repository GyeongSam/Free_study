N=int(input())
Room=[[1]*(N+2)]+[[1]+list(map(int,input().split()))+[1] for _ in '_'*N]+[[1]*(N+2)]
stack=[(1,2,0)]
cnt=0
while stack!=[]:
    I,J,d=stack.pop()
    sub=[]
    I2=I+1
    J2=J+1
    sub.append(Room[I][J2])
    sub.append(Room[I2][J2])
    sub.append(Room[I2][J])
    if sub==[0,0,0]:
        if J2==N and I2==N:cnt+=1
        else:stack.append((I2,J2,1))
    if d!=2 and sub[0]==0:
        if I==N and J2==N:cnt+=1
        else:stack.append((I,J2,0))
    if d!=0 and sub[2]==0:
        if I2==N and J==N:cnt+=1
        else:stack.append((I2,J,2))
print(cnt)