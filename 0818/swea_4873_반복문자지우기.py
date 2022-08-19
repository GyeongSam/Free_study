for T in range(1,int(input())+1):
    W=list(input())
    S=[W.pop(0)]
    while W!=[]:
        sub=W.pop(0)
        if S!=[] and sub==S[-1]:S.pop()
        else:S.append(sub)
    print(f'#{T} {len(S)}')
