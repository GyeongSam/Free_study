

N=int(input())
max=0
MAX=[]
R1=int(3*N/5) if int((3*N/5))!=0 else 1
R2=int(2*N/3)+2
for i in range(R1,R2):
    sub=[N,i]
    while sub[-2]>=sub[-1]:
        sub.append(sub[-2]-sub[-1])
    if len(sub)>max:max=len(sub);MAX=sub
print(max)
print(*MAX)


