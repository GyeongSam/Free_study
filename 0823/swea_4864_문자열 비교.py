for T in range(1,int(input())+1):
    A=input()
    B=input()
    la=len(A)
    lb=len(B)
    D_list=[{}]
    sub={}
    for i in range(la-1):
        sub[A[i]]=i
        D_list.append(sub.copy())
    print(D_list)

    i=la-1
    while i<lb:
        for d in range(la):
            print(i)
            if B[i-d]!=A[-1-d]:
                now=la-1-d
                if B[i-d] in D_list[now]:
                    i+=now-D_list[now][B[i-d]]
                    break
                else:i+=la;break
        else:
            print(f'#{T} 1')
            break
        continue
    else:print(f'#{T} 0')
    

                

