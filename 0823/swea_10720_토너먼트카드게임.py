

def RF(L):
    l=len(L)
    if l==1:    #혼자->승리자
        return L[0]
    else:
        c = (1+l)//2    #중간값
        W1=RF(L[:c])    #왼쪽 승자
        W2=RF(L[c:])    #오른쪽 승자
        f=O[W1]-O[W2]   #대결
        return W1 if f==1 or f==-2 or f==0 else W2  #오른쪽이졌으면 왼쪽 리턴

for T in range(1,int(input())+1):
    N=int(input())
    O=list(map(int,input().split()))
    print(f'#{T} {RF([i for i in range(N)])+1}')


