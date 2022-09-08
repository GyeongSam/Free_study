from django import forms
from .models import Article

#상속받으려면 대문자
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea) 

class ArticleForm(forms.ModelForm):
    title=forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title',
                'placeholder':'Enter the title',
                'maxlength':10,
            }
        )
    )
    content=forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class':'my-content',
                'placeholder':'Enter the content',
                'row':5,
                'column':50,

            }
        ),
        error_messages={
            'required':'Please 내용 입력'
        }
    )
    class Meta:
        model=Article
        fields = '__all__'
        # exclud =('title',) #
