password=input('비밀번호를 설정하세요 : ')
count=0
print('설정 완료되었습니다.')

while True:
    is_pw=input('비밀번호를 입력하세요 : ')
    if password == is_pw:
        print('열렸습니다.')
        break
    else:
        count+=1
        if count==3:
            print('틀렸습니다. 입력 횟수가 초과되어 종료합니다.')
            break
        print(f'틀렸습니다. 남은 입력 횟수는 {3-count}회 입니다.')
        
    