from django.shortcuts import render
import random
import requests
# Create your views here.


def lotto(request):
    url='https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1'
    response=requests.get(url).json()                   #api에서 정보를받아옵니다.
    c_nums=[]                                           #필요한 정보만 뽑을 리스트입니다.
    for i in range(1,7):
        c_nums.append(response.get(f'drwtNo{str(i)}'))  #1~6을 돌면서 당첨번호를 받아옵니다.
    b_num=response.get('bnusNo')                        #보너스 번호도 받습니다.
    A=[0]*8
    for i in '_'*1000:                                  #1000번 반복
        cnt=0                                           #맞은 개수를 저장할 카운트
        num = random.sample(range(1,46),6)              #랜덤 6개 번호를 뽑아서
        for j in num:                                   
            if j in c_nums:cnt+=1                       #각 번호가 당첨번호에 있다면 카운트를 올려줍니다.
        if cnt==5 and b_num in num:cnt+=2               #5개만 맞았는데, 보너스넘버가 있다면 7번 인덱스에 저장하기위해 +2하고 끝냅니다.
        A[cnt]+=1                                       #카운트의 인덱스에 저장합니다.
    context={
        'n':c_nums,
        'b':b_num,
        'r1':A[6],
        'r2':A[7],
        'r3':A[5],
        'r4':A[4],
        'r5':A[3],
        'x':sum(A[0:3]),
    }
    return render(request, 'lotto.html',context)
