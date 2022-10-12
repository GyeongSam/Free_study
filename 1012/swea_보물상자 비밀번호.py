
def to10(string):
    x=0;sum=0
    for c in string[::-1]:
        n=(ord(c)-55) if ord(c)>64 else int(c)
        sum+=n*(16**x)
        x+=1
    return sum

for t in range(1,int(input())+1):
    N,K=map(int,input().split())
    q=input()*2;s=set();c=N//4
    for i in range(N):
        s.add(q[i:i+c])
    s=sorted(list(s),key=to10,reverse=True)
    print(f'#{t}',to10(s[K-1]))

