

def leap_year(x):
    if x%4==0 and x%100!=0:
        return f'{x}년은 윤년입니다.'
    elif x%400==0:
        return f'{x}년은 윤년입니다.'
    else:
        return f'{x}년은 윤년이 아닙니다.'
