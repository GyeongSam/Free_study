from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

#기본적으로 제공하는 User 모델 말고 사용자가 만드는거 쓸거라 다시 등록해줘야함
admin.site.register(User, UserAdmin)


# Register your models here.
