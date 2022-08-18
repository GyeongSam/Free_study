l=['(','{']
r=[')','}']
d={')':'(','}':'{'}

for T in range(1,int(input())+1):
    s=input()
    S=[]
    ans=1
    for i in s:
        if i in l:
            S.append(i)
        elif i in r:
            if S==[] or d[i]!=S.pop():ans=0;break
    if S!=[]:ans=0
    print(f'#{T} {ans}')