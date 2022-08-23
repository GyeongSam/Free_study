icp={'(':3,'+':1,'*':2}
isp={'(':0,'+':1,'*':2}
for T in range(1,11):
    N=input()
    M=input()
    N=''    #후위 표기법으로 바꿀 저장공간
    stk=[]  #스택
    for i in M: #수식을 돌면서
        if i.isnumeric():   #숫자라면 N에 저장
            N+=i
        elif i==')':    #닫는 괄호를 만나면 여는 괄호 만날때까지 털어냄
            while stk[-1]!='(':
                N+=stk.pop()
            stk.pop()   #여는 괄호 버림
        else:
            n=icp[i]
            if stk==[] or n>icp[stk[-1]]: stk.append(i) #비어있거나 우선순위가 높다면 푸쉬
            else:
                while stk!=[] and isp[stk[-1]]>=n:  #아니라면 비거나 우선순위 낮은애 만날때까지 털어냄
                    N+=stk.pop()
                stk.append(i)   #그리곤 추가
    while stk!=[]:  #남은 연산자들을 털어냄
        N+=stk.pop()


    #후위표기식 완성

    for j in N: #계산
        if j.isnumeric():       #숫자면 스택에 쌓음
            stk.append(int(j))
        else:   #연산자면
            A=stk.pop()
            B=stk.pop() #스택에 쌓인 숫자 두개를 꺼내서
            sub=A*B if j=='*' else A+B
            stk.append(sub) #연산 한 값을 스택에 푸쉬
    print(f'#{T}',*stk) #남은 숫자를 출력