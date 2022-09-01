

### 1. 데이터 객체를 만드는 방법 3가지

**1. 첫번째 방법**

```shell
article = Article()
article.title = '제목'
article.content = '내용'
article.save()
```



**2. 두번째 방법**

```shell
article = Article(title='제목',content='내용')
article.save()
```



**3. 세번째 방법**

```shell
Article.objects.create(title='제목',content='내용')
```



### 2. 마이그레이션 핵심 명령어

```shell
python manage.py migrations
python manage.py migrate
```


