from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',) #회원가입시 이메일도 받음

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email','first_name','last_name',)




#AbstractUser

#AuthenticationForm
#SetPasswordForm





#UserCreationForm
#UserChangeForm
#enrosms Meta class에서 등록된 모델이 User(기본)이어서 반드시 커스텀을 해줘야함