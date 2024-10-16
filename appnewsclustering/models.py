from django.db import models

# Create your models here.

# appnewsclustering /models.py
class Company(models.Model):
    name = models.CharField(max_length=100)
    description1 = models.TextField()
    description2 = models.TextField(default="Default Description")  # 기본값 설정 (앞으로 모델 필드를 추가하더라도 해당 설정 "dfault=~"을 따로 안 해도 됨)
    founded_date = models.DateField()
    headquarters = models.CharField(max_length=200)

    def __str__(self):
        return self.name
