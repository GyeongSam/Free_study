
for T in range(1,int(input())+1):
    N=int(input())
    ans=[]
    for n in [2,3,5,7,11]:
        for i in range(100):
            if N%(n**i):
                ans.append(i-1)
                break
    print(f'#{T}',*ans)

