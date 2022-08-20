def f(L,l): #보이어 무어 알고리즘으로 문자열이 해당하는 위치를 찾습니다.
    n=len(l)
    B={x:n-i-1 for i,x in enumerate(l[:-1])}
    while n<=len(L):
        for d in range(1,len(l)+1):
            if L[n-d]!=l[-d]:
                if L[n-d] in B:
                    dn=B[L[n-d]]-d+1
                    if dn<=0:dn=len(l)
                else:dn=len(l)
                n+=dn
                break
        else:return n
    else:return -1  #없다면 -1을 반환합니다.

            
for T in range(1,int(input())+1):
    A,B=input().split()
    a=len(A)
    cnt=0   #몇 번을 찾았는지 기억
    while len(A)>=len(B):   #A가 B보다 작아질때까지 반복
        i=f(A,B)    #문자열의 위치를찾고
        if i==-1:   #없다면 멈춤
            break
        A=A[i:] #있으면 잘라냄
        cnt+=1
    print(f'#{T} {a-(len(B)-1)*cnt}')
