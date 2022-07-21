N=int(input())

def is_Div(x):
    if N%x==0:
        if x==N:
            print(x)
        print(x,end=' ')


for i in range(1,N+1):
    is_Div(i)
