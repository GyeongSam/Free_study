def B_M(A,B):
    lb=len(B)
    Bad=[{s:lb-i-j for i,s in enumerate(B[:-j])} for j in range(1,lb)]
    i=lb-1
    while i<=len(A)-1:
        for di in range(lb):
            if A[i-di]!=B[-1-di]:
                if A[i-di] in Bad[di]:
                    i+=Bad[di][A[i-di]]
                else: i+=lb
                break
        else:return i+1
    return -1
        
for T in range(1,int(input())+1):
    A,B=input().split()
    lA=len(A)
    i=0
    cnt=0
    while len(A)>=len(B):
        i=B_M(A,B)
        if i==-1:
            break
        A=A[i:]
        cnt+=1
    print(f'#{T} {lA-(len(B)-1)*cnt}')


                                
