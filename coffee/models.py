from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=50)


class Menu(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    price=models.FloatField()
    category=models.OneToOneField(Category,on_delete=models.CASCADE,related_name='menu')
    image=models.ImageField

