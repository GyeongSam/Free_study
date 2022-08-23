for T in range(1,11):
    N=input()
    M=input()
    N=''    #후위 표기법으로 바꿀 저장공간
    stk=[]  #스택

    for i in M: #수식을 돌면서
        if i.isnumeric():   #숫자라면 N에 저장
            N+=i
        else:   #연산자면
            if stk==[]:    #비어있거나 우선순위가 높은경우
                stk.append(i)   #스택에 추가
            elif i=='*':   #*는 +를 만날때까지 비우고 스택에 쌓음
                while stk!=[] and stk[-1]!='+':
                    N+=stk.pop()
                stk.append(i)
            else:
                while stk!=[]:  #그 외의 경우엔 낮은연산자가 없으므로 다비우고 스택을 쌓음
                    N+=stk.pop()
                stk.append(i)
    while stk!=[]:  #남은 연산자들을 털어냄
        N+=stk.pop()

    #후위표기식 완성

    for j in N: #계산
        if j.isnumeric():       #숫자면 스택에 쌓음
            stk.append(int(j))
        else:   #연산자면
            A=stk.pop()
            B=stk.pop() #스택에 쌓인 숫자 두개를 꺼내서
            if j=='*':
                stk.append(A*B) #연산자가 *라면 곱셈을 스택에 쌓음
            else:
                stk.append(A+B) #+라면 더해서 스택에 쌓음
    print(f'#{T}',*stk) #남은 숫자를 출력
