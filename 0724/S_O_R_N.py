
def sum_of_repeat_number(List_par):
    sum=0
    for x in set(List_par):
        if List_par.count(x)==1:
            sum+=x
    return sum
            
print(sum_of_repeat_number([4,4,7,8,10,4]))