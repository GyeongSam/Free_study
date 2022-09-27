I=lambda:map(int,input().split())
for t in range(1,int(input())+1):
    N,M=I();A=list(I());B=list(I())
    A.sort()
    cnt=0
    for b in B:
        l=0;r=N-1
        fl=0;fr=0
        while(l<=r):
            m=(l+r)//2
            if A[m]==b:cnt+=1;break
            elif A[m]<b:
                l=m+1
                if fr:break
                fl=0;fr=1
            elif A[m]>b:
                r=m-1
                if fl:break
                fr=0;fl=1
    print(f'#{t}',cnt)