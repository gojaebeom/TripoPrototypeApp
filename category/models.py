from customuser.models import CustomUser
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # 외래키 설정