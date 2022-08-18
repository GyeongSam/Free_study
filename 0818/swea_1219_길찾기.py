for t in '_'*10:
    T,N=input().split()
    L=list(input().split())
    path={} #경로를 저장 dict
    for i in range(0,2*int(N),2):
        if L[i] in path:
            path[L[i]].append(L[i+1])
        else:path[L[i]]=[L[i+1]]
    S=['0']
    V=['0']
    ans=0
    while S!=[]:
        sub=S.pop()
        if sub not in path:continue
        nxt=path[sub]
        if '99' in nxt:ans=1;break
        for i in nxt:
            if i not in V:
                S.append(i)
                V.append(i)
    print(f'#{T} {ans}')


        
        
        

    

    