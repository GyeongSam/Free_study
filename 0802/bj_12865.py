import sys
N,K=map(int, sys.stdin.readline().split())
bag=[]
for i in range(N):
    bag.append(list(map(int, sys.stdin.readline().split())))
best=[[0]*N]
for i in range(1,K+1):
    i_best=[]
    for item in bag:
        case1=i_best[-1] if i_best!=[] else 0        
        case2=best[-1][len(i_best)]
        if i_best!=[]:
            case3=best[i-item[0]][len(i_best)-1]+item[1] if i-item[0]>=0 else 0
        else:
            case3=item[1] if item[0]<=i else 0
        i_best.append(max(case1,case2,case3))
    best.append(i_best)
print(best[-1][-1])
