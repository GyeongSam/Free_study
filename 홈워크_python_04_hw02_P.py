words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

N_words=[]  #철자를 분석할 저장소

for i in words:
    N_words.append(''.join(sorted(i)))  #각 단어의 철자를 오름차순 정렬해서 저장소에 담기

dict_N_words={} #애너그램 그룹핑할 dict 저장소

for j in set(N_words):
    dict_N_words[j]=[i for i , v in enumerate(N_words) if v==j] #무엇들이 애너그램인지 판단 후 dict에 그룹핑

for value in dict_N_words.values():     #dict의 그룹핑된 value들을 순회하며
    sub=[]
    for i in value:
        sub.append(words[i])
    print(sub)      #해당 단어들을 그룹별로 출력
