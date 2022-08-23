
def err():
    print(f'#{T} error')

for T in range(1,int(input())+1):
    A=input().split()
    stk=[]
    for i in A:
        if i.isnumeric():
            stk.append(int(i))
        elif i=='.':    # . 을만나면
            try:
                ans = stk.pop() #답을 출력
                if stk!=[] or i!=A[-1]:     #했는데도 스택이 비어있지않다면
                    err();break #err 종료
                print(f'#{T} {ans}')    #정상적이라면 출력
                break
            except:
                err();break #오류발생시 종료
        else:   #연산자라면
            try:
                x = stk.pop()   #숫자 두개를 뽑고
                y = stk.pop()
                sub=x*y if i=='*' else x+y if i=='+' else x-y if i=='-' else x/y
                stk.append(sub) #stk에 연산결과를 쌓음
            except:
                err();break #오류발생시 종료


