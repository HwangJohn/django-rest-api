# -*- coding: utf-8 -*-
from django.db import models
 
class Movie(models.Model):
    title = models.CharField(max_length=30) # 제목
    genre = models.CharField(max_length=15) # 장르
    year = models.IntegerField()  # 제작 년도
