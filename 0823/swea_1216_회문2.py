def check(c):
    if c==0:
        J=j+dj
        for d in range(1,dj//2):
            if A[i][j+d]!=A[i][J-d]:
                return 0
        return 1
    else:
        I=i+di
        for d in range(1,di//2):
            if A[i+d][j]!=A[I-d][j]:
                return 0
        return 1

for _ in '_'*10:
    T=input()
    A=[list(input()) for _ in '_'*100]
    R=range(100)
    M=1
    for i in R:
        for j in R:
            sub=A[i][j]
            dj=M
            while j+dj<100:
                if A[i][j+dj]==sub and check(0):
                    M=dj+1
                dj+=1
            di=M
            while i+di<100:
                if A[i+di][j]==sub and check(1):
                    M=di+1
                di+=1
    print(T,M)
                