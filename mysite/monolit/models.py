from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=100, verbose_name='Логин', unique=True)
    avatar = models.ImageField(verbose_name='Аватар', upload_to='avatars/', blank=False)
    userInfo = models.TextField(max_length=1000, verbose_name='Обо мне', blank=False)

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название товара', blank=False)
    productImage = models.ImageField(verbose_name='Изображение товара', upload_to='productImages/', blank=False)
    description = models.TextField(max_length=1000, verbose_name='Описание товара', blank=False)
    date_create = models.DateField(default=datetime.now, verbose_name="Дата создания")
    time_create = models.TimeField(default=datetime.now, verbose_name="Время создания")

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Корзина пользователя {self.user.username}  | Продукт {self.product.title}'



