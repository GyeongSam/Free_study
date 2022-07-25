
def num_swap(L,n,m):
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j]==n:
                L[i][j]=m
            elif L[i][j]==m:
                L[i][j]=n
    return L

def hanoi(N):
    if N==1:
        return [[1,3]]
    else:
        return num_swap(hanoi(N-1),2,3)+[[1,3]]+num_swap(hanoi(N-1),1,2)

N=int(input())
X=hanoi(N)
print(len(X))
for x in X:
    print(x[0],x[1])