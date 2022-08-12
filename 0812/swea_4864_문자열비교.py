for T in range(1,int(input())+1):
    A=input()
    B=input()
    s=0
    for i in range(len(B)-len(A)+1):
        print(B[i:i+len(A)])
        if A==B[i:i+len(A)]:s=1
    print(f'#{T} {s}')