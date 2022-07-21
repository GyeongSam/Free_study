students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']
dict_students={}

for i in set(students):
    dict_students[i]=students.count(i)

sorted_dict_students=sorted(dict_students.values(), key=lambda x : x**2, reverse=True)

print(sorted_dict_students)
