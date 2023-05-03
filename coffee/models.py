from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Table(models.Model):
    quantity = models.IntegerField()
    booking = models.BooleanField(default=True)
    who_book = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    data = models.DateTimeField()
    email = models.EmailField()

    def __str__(self):
        return self.who_book


class Staff(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    position = models.CharField(max_length=50)
    number = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):
        return self.name
