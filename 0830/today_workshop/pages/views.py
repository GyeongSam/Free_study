import re
from django.shortcuts import render
from datetime import datetime
import random

# Create your views here.
def index(request):
    return render(request,'index.html')

def greeting(request):
    foods=['apple','banana','coconut']
    info = {
        'name':'32'
    }
    context = {
        'foods':foods,
        'info':info,
    }
    return render(request, 'greeting.html', context)

def dinner(request, food,num):
    context={
        'food':food,
        'num':num,
    }
    return render(request, 'dinner.html',context)


    return render(request, 'dinner.html',context)

def image(request):

    return render(request,'image.html')

def template_language(request):
    menus =['떡볶이','파스타','순대국밥','스테이크','쭈꾸미볶음','짜장면','물이나','생선구이','제육볶음','가지무침']
    my_sentence = 'Music is my life, music is my life'
    messages = ['apple','banana','cocumber','mango']
    empty_list = []
    datetimenow = datetime.now()
    
    context = {
        'menus':menus,
        'my_sentence':my_sentence,
        'messages':messages,
        'empty_list':empty_list,
        'datetimenow':datetimenow,
    }
    return render(request, 'template_language.html',context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    print(request)
    print(type(request))
    print(request.GET)
    print(request.GET.get('message'))
    message=request.GET.get('message')

    context = {
        'message':message
    }
    return render(request, 'catch.html',context)
def hello(request, name,age):
    context={
        'name':name,
        'age':age,
    }
    return render(request, 'hello.html',context)

def lotto(request):
    lotto_1030=[2,5,11,17,24,29]
    lotto_random=random.sample(range(1,46),6)
    ok=[i for i in lotto_random if i in lotto_1030]
    ok_len=len(ok)
    context={
        'lotto_1030':lotto_1030,
        'lotto_random':lotto_random,
        'ok':ok,
        'ok_len':ok_len,
    }
    return render(request, 'lotto.html',context)