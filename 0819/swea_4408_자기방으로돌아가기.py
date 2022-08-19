
for T in range(1,int(input())+1):
    N=int(input())
    L=[list(map(lambda x:-(-int(x)//2),input().split())) for _ in '_'*N]
    L.sort(key=lambda x:max(x))
    cnt=0
    while L!=[]:
        print(L)
        cnt+=1
        e=L.pop(0)
        i=0
        while i<len(L):
            if min(L[i])>max(e):e=L.pop(i)
            else: i+=1
    print(f'#{T} {cnt}')

