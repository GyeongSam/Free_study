N=int(input());M=max
L=list(map(int, input().split()))
inc=[0]*N
dec=[0]*N
for i in range(N):
    inc_sub=0
    dec_sub=0
    for j in range(i):
        if L[i]>=L[j] and inc[j]>=inc_sub:inc_sub=inc[j]
        if L[i]<=L[j] and dec[j]<=dec_sub:dec_sub=dec[j]
    inc[i]=inc_sub+1
    dec[i]=dec_sub+1
print(inc)
print(dec)
print(max(max(inc),max(dec)))



