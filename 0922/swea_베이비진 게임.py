def is_win(L):
    for i in range(len(L)):
        if i>=2 and L[i-2]==L[i-1]==L[i]:return 1
    sub=sorted(list(set(L)))
    for i in range(2,len(sub)):
        if sub[i-2]+2==sub[i-1]+1==sub[i]:return 1
    return 0

for t in range(1,int(input())+1):
    L=list(map(int,input().split()))
    l=len(L)
    p1=[]
    p2=[]
    for i in range(l):
        if i%2:
            p2.append(L[i]);p2.sort()
            if len(p2)>2 and is_win(p2):print(f'#{t}',2);break
        else:
            p1.append(L[i]);p1.sort()
            if len(p1)>2 and is_win(p1):print(f'#{t}',1);break
    else:print(f'#{t}',0)
