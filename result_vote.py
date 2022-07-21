
students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']
dict_students={}

for i in set(students):
    dict_students[i]=students.count(i)

sorted_dict_students=sorted(dict_students.items(), key=lambda item : item[1], reverse=True)

for _ in sorted_dict_students:
    print(f'{_[0]}는(은)) {_[1]}득표 했습니다.')
