from .models import Article
from django.shortcuts import render, redirect
from .forms import ArticleForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm() #form->객체
#     context={
#         'form':form,
#     }
#     return render(request, 'articles/new.html',context)
@login_required
@require_http_methods(["GET","POST"])
def create(request):
    #5. create 요청(POST) -> 사용자가 데이터 입력 후, 저장 요청 -> 근데 잘못됨
    #10. '' 올바른 요청
    if request.method=='POST':
        #6. ArticleForm 인스턴스화 -> 데이터가 입력되어있는 종이 만들기
        #11. ArticleForm을 인스턴스화

        form = ArticleForm(request.POST)
        #7. 데이터 유효 검증(잘못된 데이터라 실패)
        #12. 성공
        if form.is_valid():
            #13. 데이터 저장
            article=form.save()
            #14. 원하느 경로로 redirect
            return redirect('articles:detail',article.pk)
            



    else:       #1. 사용자가 create 경로로 요청을 보냄(GET) -> 빈종이 달라
                #2. ArticleForm으로 빈종이 만든다.
        form = ArticleForm()
                #3. 사용자에게 빈종이를 보내주기 위해서 context 담기
    #8. 유효한 데이터만 들어있는 종이를 다시 돌려 주기 위해 context에 담기

    context = {
        'form':form,
    }
                #4. 사용자에게 빈종이를 넘겨준다.
    #9. 사용자에게 올바른 데이터만 들어있는 종이를 다시 넘겨준다.
    return render(request, 'articles/create.html', context)
    
    
    
    # form = ArticleForm(request.POST)
    # if form.is_valid():
    #     article = form.save()
    #     return redirect('articles:detail',article.pk )
    #     # form.save()
    #     # return redirect('articles:index')
    # print(f'에러: {form.errors}')
    # context={
    #     'form':form,
    # }
    # return render(request,'articles:new.html',context)


    # title = request.POST.get('title') 
    # content = request.POST.get('content')

    # 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2.
    # article = Article(title=title, content=content)
    # article.save()

    # 3. 
    # Article.objects.create(title=title, content=content)

    # return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('articles:index')
    

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form':form,
#     }
#     return render(request, 'articles/edit.html', context)
@login_required
@require_http_methods(["GET","POST"])
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    
    context={
        'form':form,
        'article':article,
    }
    return render(request, 'articles/update.html',context)
    
    # article = Article.objects.get(pk=pk)
    # form = ArticleForm(request.POST, instance=article)
    # if form.is_valid():
    #     form.save()
    #     return redirect('articles:detail',article.pk)
    
    # context = {
    #     'form':form,
    #     'article':article,

    # }
    # return render(request,'articles/edit.html',context)



    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)
