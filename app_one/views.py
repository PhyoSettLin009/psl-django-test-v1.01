from django.shortcuts import render



def index(request):
    return render(request,'app_one/index.html')



def user_login(request):
    return render(request,'app_one/login.html')



def user_register(request):
    return render(request,'app_one/register.html')



def my_test(request):
    return render(request,'app_one/test.html')