from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):  # 요청을받고
    # return HttpResponse("hello world")    # 직접 html을 만들어서 보여줌
    return render(request, 'accountapp/hello_world.html')    # accountapp/hello_world.html에 집어넣어서 보여줌 
