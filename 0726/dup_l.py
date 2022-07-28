def duplicated_letters(str_par):
    new_list=[]
    for i in set(str_par):  #str_par의 중복되지않는 요소들을 순회하면서
        if str_par.count(i)>1:  #str_par의 개수가 1개초과라면
            new_list.append(i)  #new_list에 요소를 추가해서
    return new_list             #반환합니다.

print(duplicated_letters('apple')) #['p']
print(duplicated_letters('banana')) #['n', 'a']