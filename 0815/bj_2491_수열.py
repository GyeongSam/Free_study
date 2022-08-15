N=int(input())
inc=1;dec=1
cnt_i=cnt_d=1
L=list(map(int,input().split()))
for i in range(1,N):
    if L[i-1]<=L[i]:
        cnt_i+=1
        if cnt_i>inc:inc=cnt_i
    else:
        cnt_i=1
    if L[i-1]>=L[i]:
        cnt_d+=1
        if cnt_d>dec:dec=cnt_d
    else:
        cnt_d=1

    print(cnt_i,cnt_d,inc,dec)
print(max(inc,dec))
