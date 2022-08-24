for _ in '_'*10:
    T=input()
    L=list(map(int,input().split()))
    while True:
        for i in range(1,6):
            sub=L.pop(0)-i
            if sub<=0:L.append(0);break
            L.append(sub)
        else:continue
        break
    print(*L)
