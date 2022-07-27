
def Collatz(N,cnt=0):
    if N==1:
        return cnt
    elif cnt==500:
        return -1
    else:
        return Collatz(N/2,cnt+1) if N%2==0 else Collatz(3*N+1,cnt+1)

print(Collatz(6))
