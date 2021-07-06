from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100) # 카테고리 이름
    


