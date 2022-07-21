a=input()
L=[]
for i in a:
    if i.isnumeric():
        L.append(int(i))    #[a,b,c...] 와 같은 입력이 들어와도 list 형식으로 숫자만 저장하기

s_num=L[0]
new_L=[L[0]]
for i in L[1:]:
    if s_num==i:
        continue
    s_num=i
    new_L.append(s_num)
    
print(new_L)
