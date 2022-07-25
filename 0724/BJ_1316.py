N=int(input())
cnt=0
for n in range(N):
    S=input()
    stnd=S[0]
    for i in S[1:]:
        if stnd[-1]==i:
            continue
        else:
            stnd+=i
    if len(set(list(S)))==len(stnd):
        cnt+=1
print(cnt)
            
