def sum_list_while(numbers):
    cnt=0
    S=0
    while cnt<len(numbers):
        S+=sum(numbers[cnt])
        cnt+=1
    return S

print(sum_list_while([[1, 4], [10, 5], [20, 30]]))