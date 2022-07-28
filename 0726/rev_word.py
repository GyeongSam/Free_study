words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

def in_word(word):
    if word[0]=='b' or word[0]=='m' or word[0]=='p':
        return 'im'+word
    elif word[0]=='l':
        return 'il'+word
    elif word[0]=='r':
        return 'ir'+word
    else:
        return 'in'+word        #영어 반의어 만드는 함수

def Hin_word(word):
    if word[-1]=='인':
        return word[:len(word)-1]+'이지 않은'
    elif word[-1]=='한':
        return word[:len(word)-1]+'하지 않은'
    elif word[-1]=='는':
        return word[:len(word)-1]+'지 않은'
    else:
        return '불'+word        #한글 설명 반의어로 바꾸는 함수


ant_words_dict={}   #반의어를 저장할 dict
for key,value in words_dict.items():    #dict의 items를 순회하면서
    ant_words_dict[in_word(key)]=Hin_word(value) #반의어로 바꾼 후 저장

for i in sorted(ant_words_dict.items()): #오름차순 정렬된 반의어를 출력
    print(f'{i[0]} : {i[1]}')
