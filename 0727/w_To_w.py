words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]

def wordrelay(L):
    said_words=[L[0]]
    cnt=1
    for i in words[1:]:
        cnt+=1
        if i[0]!=said_words[-1][-1] or i in said_words:
            return f'{cnt}번째 참가자가 탈락하였습니다.'
        elif i=='done':
            return '끝말잇기 종료'
        else: said_words+=[i]


print(wordrelay(words)) # 5번째 참가자가 탈락하였습니다.