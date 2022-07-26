N=int(input())
def sum_of_digit(N):
    s=0
    for i in str(N):
        s+=int(i)
    return s
print(sum_of_digit(N))