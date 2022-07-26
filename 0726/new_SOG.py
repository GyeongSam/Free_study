N=int(input())
def sum_of_digit(N):
    return sum(list(map(int, list(str(N)))))

print(sum_of_digit(N))

