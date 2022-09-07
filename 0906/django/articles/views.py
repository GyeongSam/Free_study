from django.shortcuts import render
from .models import Article



def index(request):
    articles=Article.objects.all()[::-1]
    context={
        'articles':articles
    }
    return render(request,'index.html',context)

def new(request):
    return render(request,'new.html')

def create(request):
    title=request.POST.get('title')
    content=request.POST.get('content')
    article=Article(title=title,content=content)
    article.save()
    return render(request,'create.html')

# Create your views here.
