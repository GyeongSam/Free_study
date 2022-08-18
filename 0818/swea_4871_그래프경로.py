for T in range(1,int(input())+1):
    V,M=input().split()
    path={}
    for _ in '_'*int(M):
        st,ed=input().split()
        if st in path:
            path[st].append(ed)
        else:
            path[st]=[ed]
    print(path)
    vi,ar=input().split()
    V=[vi]
    ans=0
    while V!=[]:
        sub=V.pop()
        if sub in path:A=path[sub]
        else:continue
        if ar in A:ans=1;break
        V+=A
        print(V)
    print(f'#{T} {ans}')

            

            


