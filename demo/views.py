from django.shortcuts import render
from .models import user
from django.http import HttpResponse
# Create your views here.

def fun1(request):
    usertest=user.objects.all()
    # for item in usertest:
    #     print(item.email)
    # print(usertest.user())
    # name='Lalan Ranjan'
    # name='Lalan Ranjan'
    # email='lranjan@petrabytes.com'
    Dict={'userlist':usertest}
    return render(request,'demo/home.html',Dict)
    # return HttpResponse('Hi All!')

def fun2(request,slug):
    slug=slug
    usertest=user.objects.get(slug=slug)
    print(usertest.name)
    print(usertest.Address)
    Dict={'usertest':usertest}
    return render(request,'demo/test.html',Dict)
    # print(slug)