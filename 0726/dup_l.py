def duplicated_letters(str_par):
    new_list=[]
    for i in set(str_par):
        if str_par.count(i)>1:
            new_list.append(i)
    return new_list

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))