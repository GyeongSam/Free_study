N=int(input())
for i in range(N-1):
    print(' '*(N-1-i)+'*'*(i+1))
for i in range(N)[::-1]:
    print(' '*(N-1-i)+'*'*(i+1))
