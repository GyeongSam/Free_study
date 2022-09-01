from email import contentmanager
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #최초생성일
    updated_at = models.DateTimeField(auto_now=True)    #최종수정

    def __str__(self):
        return f'{self.title} / {self.content}'

