from webbrowser import get


def get_secret_number(x):
    sum=0
    for i in list(x):
        sum+=ord(i)
    return sum

print(get_secret_number('dixon'))