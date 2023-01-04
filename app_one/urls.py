from django.urls import path
from app_one import views

app_name = 'my_urls'

urlpatterns = [
    path('',views.index,name='my_index'),
    path('user_login',views.user_login,name='user_login'),
    path('user_register',views.user_register,name='user_register'),
    path('my_test',views.my_test,name='my_test'),
]