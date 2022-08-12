D={'ZRO':0,'ONE':1,'TWO':2,'THR':3,'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
for t in range(int(input())):
    T,M=input().split()
    L=list(input().split())
    ans=[0]*10  #문자열 카운트할 공간
    for i in L: #인풋 순회하면서 카운트
        ans[D[i]]+=1
    print(T)
    for k,v in D.items():   #Dict를 순회
        for _ in range(ans[v]): #ans 카운트만큼 반복
            if _==ans[v]-1 and k=='NIN': #끝항이면 다음줄로 넘어가고
                print(k)
            else:print(k,end=' ') #아니면 스페이스바 인쇄



