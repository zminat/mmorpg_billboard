from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


class Ad(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    CATEGORY_CHOICES = (
        ('TA', 'Танки'),
        ('HI', 'Хилы'),
        ('DD', 'ДД'),
        ('DE', 'Торговцы'),
        ('GM', 'Гилдмастеры'),
        ('QG', 'Квестгиверы'),
        ('BS', 'Кузнецы'),
        ('TA', 'Кожевники'),
        ('PM', 'Зельевары'),
        ('SM', 'Мастера заклинаний'))

    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, verbose_name='Категория')
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = CKEditor5Field(verbose_name='Текст', config_name='extends')
    upload = models.FileField(upload_to='uploads/')


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)
