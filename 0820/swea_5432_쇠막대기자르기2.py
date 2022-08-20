for T in range(1,int(input())+1):
    L=input().replace('()','*')
    bar=0
    cnt=0
    for i in range(len(L)):
        if L[i]=='(':
            bar+=1
            cnt+=1
        elif L[i]==')':
            bar-=1
        elif L[i]=='*':
            cnt+=bar
    print(f'#{T} {cnt}')