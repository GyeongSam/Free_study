I=input
for t in range(1,int(I())+1):
    L=[list(map(int,I().split())) for _ in '_'*int(I())]
    L.sort(key=lambda x:x[1])
    c=1;a=L[0][1]
    for l in L:
        if l[0]>=a:a=l[1];c+=1
    print(f'#{t}',c)
