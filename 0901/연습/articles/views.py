from django.shortcuts import render, redirect
from .models import Article


# Create your views here.

def index(request):
    articles = Article.objects.all()[::-1]
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html',context)
    
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content=request.POST.get('content')

    #1
    #article = Article()

    article=Article(title=title,content=content)
    article.save()

    # return redirect('articles:index')
    return redirect('articles:detail',article.pk)

    # def create(request):
#     title = request.GET.get('title')
#     content=request.GET.get('content')

#     #1
#     #article = Article()

#     article=Article(title=title,content=content)
#     article.save()

#     return redirect('articles:index')
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,

    }
    return render(request, 'articles/detail.html',context)

def delete(request,pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/edit.html', context)

def update(request,pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title') #새로 입력한 title을 기존에 덮어쓰기
    article.content = request.POST.get('content') #새로 입력한 content를 기존 데이터에 덮어쓰기
    article.save() #DB에 데이터 저장
    return redirect('articles:detail', article.pk)
    