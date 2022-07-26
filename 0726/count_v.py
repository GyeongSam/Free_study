def count_vowels(word):
    cnt=0
    for i in 'aeiou':
        cnt+=word.count(i)
    return cnt

print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3
