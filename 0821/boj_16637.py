def cal(case):
    copy_q=q[::]
    for i in case[::-1]:
        B=copy_q.pop(i)
        C=copy_q.pop(i)
        if B=='*':
            copy_q[i-1]*=C
        elif B=='+':
            copy_q[i-1]+=C
        elif B=='-':
            copy_q[i-1]-=C
    for _ in '_'*(num_oper-len(case)):
        B=copy_q.pop(1)
        C=copy_q.pop(1)
        if B=='*':
            copy_q[0]*=C
        elif B=='+':
            copy_q[0]+=C
        elif B=='-':
            copy_q[0]-=C
    return copy_q[0]

N=int(input())
q=list(input())
for j in range(N):
    if j%2==0:q[j]=int(q[j])
oper_index=[i for i in range(N) if i%2]
num_oper=N//2
oper_combi=[[[]]]
max_choice=-(-num_oper//2)

ans=-2**31

for _ in '_'*max_choice:
    sub=[]
    for combi in oper_combi[-1]:
        for i in oper_index:
            if combi==[]:sub.append(combi+[i])
            elif i>combi[-1]+2:sub.append(combi+[i])
    oper_combi.append(sub)

for x in oper_combi:
    for case in x:
        result=cal(case)
        if result>ans:ans=result

print(ans)