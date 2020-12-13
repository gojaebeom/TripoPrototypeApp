from category.models import Category
from django.db import models
from customuser.models import CustomUser

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # 외래키 설정
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)