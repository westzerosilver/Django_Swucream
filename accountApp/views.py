from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
# hello world를 출력하는 함수
def hello_world(request) :
    return HttpResponse('Hello World!')