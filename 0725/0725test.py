def count_vowels(str_par):
    cnt=0
    for i in ['a','e','i','o','u']:
        if i in list(str_par):
            cnt+=str_par.count(i)
    return cnt

print(count_vowels('apple'))
print(count_vowels('banana'))
