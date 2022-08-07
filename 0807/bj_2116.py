o=[5,3,4,1,2,0]
    
def opp(n):
    return o[n]
def opp_num(n,i):
    return L[i][opp(L[i].index(n))]
def max_num(n,i):
    return max([x for x in L[i] if x!=n and x!=opp_num(n,i)])

L=[list(map(int,input().split())) for _ in range(int(input()))]

s=[0]*6
t=[1,2,3,4,5,6]

for i in range(len(L)):
    for j in range(6):
        s[j]+=max_num(t[j],i)
        t[j]=opp_num(t[j],i)

print(max(s))        

