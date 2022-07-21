words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

words_list=[]
for new_word in words:
    if (new_word=='done'):
            break
    if (len(words_list)!=0):
        if (new_word in words_list) or (TO_words[-1]!=new_word[0]):
            break
    TO_words=new_word
    words_list.append(new_word)

if new_word!='done':
    print(f'{len(words_list)+1}번째 사람이 탈락했습니다!')