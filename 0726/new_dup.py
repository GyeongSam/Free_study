def duplicated_letters(word):
    return [i for i in set(word) if word.count(i)>1]

print(duplicated_letters('apple')) #['p']
print(duplicated_letters('banana')) #['a', 'n']