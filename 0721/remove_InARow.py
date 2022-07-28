a=input()
L=[]
for i in a:
    if i.isnumeric():
        L.append(int(i))    #[a,b,c...] 와 같은 입력이 들어와도 list 형식으로 숫자만 저장하기

s_num=L[0]  #비교용 기준 값
new_L=[L[0]] #새로 만들 리스트
for i in L[1:]:     #기준 값과 같다면 생략 아니라면 갱신하고 새 리스트에 담기
    if s_num==i:
        continue
    s_num=i
    new_L.append(s_num)
    
print(new_L)
