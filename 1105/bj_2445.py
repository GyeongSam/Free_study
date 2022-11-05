N=int(input())
for i in range(N-1):
    print('*'*(i+1)+' '*(2*(N-1-i))+'*'*(i+1))
for i in range(N)[::-1]:
    print('*'*(i+1)+' '*(2*(N-1-i))+'*'*(i+1))
        