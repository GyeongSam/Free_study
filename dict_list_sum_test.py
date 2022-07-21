def dict_list_sum(x):
    sum=0
    for i in x:
        sum+=i['age']
    return sum

print(dict_list_sum([{'name':'kim','age':12},{'name':'lee','age':4}]))
