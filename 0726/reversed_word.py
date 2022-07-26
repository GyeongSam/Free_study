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

ant_words_dict={}   #반의어를 저장할 dict
for key,value in words_dict.items():    #dict의 items를 순회
    a=''
    if key[0]=='b' or key[0]=='m' or key[0]=='p':
        a='im'.join(key)
    elif key[0]=='l':
        a='il'.join(key)
    elif key[0]=='r':
        a='ir'.join(key)
    else:
        a='in'.join(key)
                            #영단어의 앞 철자에 따라 붙일 접두사 고르기
    
    if value[-1]=='인':
        ant_words_dict[a]=value[0:len(value)-1]+'이지 않은'
    elif value[-1]=='한':
        ant_words_dict[a]=value[0:len(value)-1]+'하지 않은'
    elif value[-1]=='는':
        ant_words_dict[a]=value[0:len(value)-1]+'지 않은'
    else:
        ant_words_dict[a]='불'.join(value)
                                                #한글 설명에 따라 설명 바꿔서 반의어 dict에 저장

for i in sorted(ant_words_dict.items()):    #오름차순 정렬된 반의어를 출력
    print(f'{i[0]} : {i[1]}')
