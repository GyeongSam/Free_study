N=int(input())
L=map(int,input().split())
M=int(input())
A=[(i,v) for i,v in enumerate(L)]
B=sorted(A,key=lambda x:(M//x[1])*1000+x[0],reverse=True)


n=M//B[0][1]

if not B[0][0]:
    
    ans1=[B[1][0]]*(M//B[1][1])
    M1=M%B[1][1]
    for n2 in range(n-1,0,-1):
        M2=M-n2*B[0][0]
        for a in A[::-1]:
            if a[0]==0: continue
            if M2>=a[0]:
                ans2=[a[0]]+[0]*n2
                M2=M2-a[0]
                break
        else:continue
        break
    if len(ans1)>len(ans2):
        ans=ans1
        M=M1
    elif len(ans1)<len(ans2):
        ans=ans2
        M=M2
    else:
        if ans1[0][0]>=ans1[0][1]:
            ans=ans1
            M=M1
        else:
            ans=ans2
            M=M2
else:
    ans=[B[0][1]]*n
    M=M%B[0][1]

print(ans)
