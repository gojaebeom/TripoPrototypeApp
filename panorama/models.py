from django.db import models

# Create your models here.
class PanoramaPost(models.Model):
    title = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to="%Y%m%d")
    image_origin_name = models.CharField(max_length=200, null=False)
    bgm = models.ImageField(upload_to="%Y%m%d") 