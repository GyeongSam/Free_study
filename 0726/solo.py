def lonely(list_par):
    return [list_par[0]]+[list_par[i] for i in range(1,len(list_par)) if list_par[i]!=list_par[i-1]]

print(lonely([1, 1, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))