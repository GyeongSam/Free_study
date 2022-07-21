def my_avg(*arg):
    sum=0
    for i in arg:
        sum+=i
    return sum/len(arg)

print(my_avg(77, 83, 95, 80, 70))