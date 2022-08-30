from django.shortcuts import render

# Create your views here.
def dinner(request, food, num):
    context={
        'food':food,
        'num':num,
    }
    return render(request, 'dinner.html',context)