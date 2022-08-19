
for T in range(1,int(input())+1):
    L=input()
    bar=cnt=sub=0
    R=len(L)-1
    for i in range(R+1):
        if sub==1:sub=0;continue
        if L[i]=='(':
            if i!=R and L[i+1]==')':
                cnt+=bar
                sub=1
                continue
            bar+=1
            cnt+=1
        elif L[i]==')':
            bar-=1
    print(f'#{T} {cnt}')