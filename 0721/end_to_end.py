print('끝말잇기를 시작합니다. 게임을 끝내시려면 done을 입력해주세요')
words_list=[]
while True: 
    new_words=input('다음 단어를 말해주세요! : ')
    if (new_words=='done'):
            print('끝말잇기를 종료합니다')
            break
    if (len(words_list)!=0):
        if (new_words in words_list) or (TO_words[-1]!=new_words[0]):
            print('게임이 끝났습니다!')
            break
    TO_words=new_words
    words_list.append(new_words)

if new_words!='done':
    print(f'{len(words_list)+1}번째 사람이 탈락했습니다!')