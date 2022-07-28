
def get_strong_number(x,y):
    sum_x=sum_y=0
    for i in list(x):
        sum_x+=ord(i)
    for j in list(y):
        sum_y+=ord(j)
    if sum_x>sum_y:
        return x
    elif sum_x<sum_y:
        return y
    else:
        return x,y
    
print(get_strong_number('delilah','dixon'))

