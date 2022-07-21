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

ant_words_dict={}
for key,value in words_dict.items():
    a=''
    if key[0]=='b' or key[0]=='m' or key[0]=='p':
        a='im'
    elif key[0]=='l':
        a='il'
    elif key[0]=='r':
        a='ir'
    else:
        a='in'
    
    if value[-1]=='인':
        ant_words_dict[a+key]=value[0:len(value)-1]+'이지 않은'
    elif value[-1]=='한':
        ant_words_dict[a+key]=value[0:len(value)-1]+'하지 않은'
    elif value[-1]=='는':
        ant_words_dict[a+key]=value[0:len(value)-1]+'지 않은'
    else:
        ant_words_dict[a+key]='불'+value

for i in sorted(ant_words_dict.items()):
    print(f'{i[0]} : {i[1]}')
