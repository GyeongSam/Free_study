from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='indext'),
    path('greeting/',views.greeting, name='greeting'),
    path('dinner/<str:food>/<int:num>/',views.dinner),
    path('image/',views.image, name='image'),
    path('template_language/',views.template_language),
    path('throw/',views.throw),
    path('catch/', views.catch),
    path('hello/<str:name>/<int:age>/',views.hello),
    path('lotto',views.lotto),
    
]
# path('ispal/<str:word>/',views.ispal),
#     path('isbirth/<int:mon>/<int:day>',views.ispal),