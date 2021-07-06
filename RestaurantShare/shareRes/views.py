from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    categories = Category.objects.all()
    content = {'categories': categories}

    # return HttpResponse("index")
    return render(request, 'shareRes/index.html',content) # 해당 html파일 실행

def restaurantDetail(request):
    # return HttpResponse("restaurantDetail")
    return render(request, 'shareRes/restaurantDetail.html')

def restaurantCreate(request):
    # return HttpResponse("restaurantCreate")
    return render(request, 'shareRes/restaurantCreate.html')

def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories' : categories}
    # return HttpResponse("categoryCreate")
    return render(request, 'shareRes/categoryCreate.html', content)

def Create_category(request):
    category_name = request.POST['categoryName'] # 사용자가 입력한 값을 POST받음
    new_category = Category(category_name = category_name) # 객체생성
    new_category.save() # 디비에 저장
    return HttpResponseRedirect(reverse('index')) # urls.py에서 설정해준 name에 따라 리디렉션 가능
    # return HttpResponse("create_category")

def Delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id = category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))




