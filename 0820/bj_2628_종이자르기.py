J,I=map(int,input().split())
# P=[[1]+[0]*(x-1)+[1] for x in (I,J)]
P=[[0,I],[0,J]]
N=int(input())
for i in '_'*N:
    s,c=map(int,input().split())
    P[s].append(c)
for i in (0,1):
    P[i].sort()
    P[i]=[x-y for x,y in zip(P[i][1:],P[i][:-1])]
print(max(P[0])*max(P[1]))
