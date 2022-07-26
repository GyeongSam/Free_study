def low_and_up(word):
    
    return ''.join([word[i].lower() if i%2==0 else word[i].upper() for i in range(len(word))])

print(low_and_up('apple')) #
print(low_and_up('banana')) #