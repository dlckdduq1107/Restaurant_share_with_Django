
from django.urls import path, include
from . import views

urlpatterns = [
    path('send/', views.sendEmail) # send로 받은 url을 가지고 이메일 전송 함수 실행(local:8000/sendEmail/send)
]