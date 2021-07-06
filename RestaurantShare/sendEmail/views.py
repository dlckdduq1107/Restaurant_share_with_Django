from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def sendEmail(request):
    return HttpResponse("sendEmail") # 화면에 sendEmail출력
