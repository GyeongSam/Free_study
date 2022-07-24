def fn_d(n):
    return sum([int(i) for i in str(n)])+n

def is_selfnumber(n):
    cnt=0
    for i in range(1,n+1):
        if fn_d(i)==n:
            cnt+=1
    return True if cnt==0 else False