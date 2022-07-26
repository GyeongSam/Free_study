def group_anagrams(L):
    L_anal_group=[]
    while len(L)>0:     #L의 항이 남아있는동안 반복
        L_sub=[L.pop(0)]    #리스트의 앞항을 하나를 뽑아서
        for i in range(len(L)-1,-1,-1): #뒤에서부터 앞으로 순회
            if sorted(list(L[i]))==sorted(list(L_sub[0])):  #뽑았던 것과 같은 애너그램이 있다면
                L_sub.insert(1,L.pop(i))    #뽑아서 sub에 임시저장
        L_anal_group.append(L_sub)      #다뽑은 것들을 리스트형태로 반환용 리스트에 저장               
    return L_anal_group #반환
print(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))

'''
def group_anagrams(L):
    L_anal_group=[]
    while len(L)>0:
        L_sub=[L.pop(0)]
        members=[]
        for i in range(len(L)):
            if sorted(list(L[i]))==sorted(list(L_sub[-1])):
                members+=[i]
        for j in reversed(members):
            L_sub.append(L.pop(j))
        L_anal_group.append(L_sub)                
    return L_anal_group
print(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
'''
