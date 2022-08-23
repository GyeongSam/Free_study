for T in range(1,int(input())+1):
    A=input().split()
    stk=[]
    end=0
    for i in A:
        if i.isnumeric():   # i가 숫자라면
            stk.append(int(i))  # 푸쉬
        elif i=='.':
            if len(stk)==1 and i==A[-1]:   #i가 점이고 끝이면서 항이 하나만 남았다면
                print(f'#{T}',int(stk[0]))
                end=1
            else: break
        elif i in ['+','*','-','/']:
            if len(stk)>=2:    #스택에 숫자가 두개이상 있고 연산자라면
                x=stk.pop()
                y=stk.pop()     #두 숫자를 뽑음
                if i=='/' and x==0: #Zero div 일경우 에러
                    break
                sub=x+y if i=='+' else x*y if i=='*' else y-x if i=='-' else y/x
                stk.append(sub)     #아닐경우 연산을 stk에 추가
            else: break
    if end==0:
        print(f'#{T} error')  #다른 모든 경우 에러 종료











