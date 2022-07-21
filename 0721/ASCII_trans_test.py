
def get_secret_word(x):
    word=''
    for i in x:
        word+=chr(i)
    return word

print(get_secret_word([83,115,65,102,89]))
