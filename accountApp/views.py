from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
# hello world를 출력하는 함수
def hello_world(request) :
    #return HttpResponse('Hello World!')    # 응답을 view에서 직접 만들어주는 방식
    #return render(request, 'base.html')     # 템플릿을 가지고 와서 내용을 채워주는 형식
    return render(request, 'accountApp/hello_world.html')   # accountApp 내의 html 파일 불러옴
