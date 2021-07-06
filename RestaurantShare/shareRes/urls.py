
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'), # local 8000의 기본화면
    path('restaurantDetail/', views.restaurantDetail, name='resDetailPage'), # local 8000/restaurantDetail의 화면
    path('restaurantCreate/', views.restaurantCreate, name='resCreatePage'),
    path('categoryCreate/', views.categoryCreate, name='cateCreatePage'),
    path('categoryCreate/create',views.Create_category, name='cateCreate'),
    path('categoryCreate/delete',views.Delete_category, name='cateDelete'),
]