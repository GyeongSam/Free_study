import sys
I=lambda:map(int,sys.stdin.readline().split())
N,M=I()
a='Yes'
for _ in '_'*M:
    b=300000
    sub=int(input())
    for i in list(I()):
        if i>b:a='No';break
        b=i
print(a)