
def all_list_sum(x):
    sum=0
    for i in x:
        for j in i:
            sum+=j
    return sum

print(all_list_sum([[1],[2,3],[4,5,6],[7,8,9,10]]))
