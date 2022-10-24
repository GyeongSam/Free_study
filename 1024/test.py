N=5
cnt=0
L=[]
def P(n):                   
    global cnt
    if (n==N): cnt+=1
    for i in range(5):  # 0~5 돌면서
        if i not in L:  # 아무것도 안뽑았던 거라면
            L.append(i) 
            P(n+1)
            L.pop()
P(0)
print(cnt)





N=5
cnt=0
DP=[0]*(1<<5)
L=[]
def P(n,visit):                   
    global cnt
    if (n==N): cnt+=1
    
    if DP[visit]:return DP[visit]

    for i in range(5):  # 0~5 돌면서
        if i not in L:  # 아무것도 안뽑았던 거라면
            L.append(i) 
            P(n+1,visit|(1<<i))
            L.pop()

P(0)
print(cnt)