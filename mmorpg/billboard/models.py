from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


class Ad(models.Model):
    """Ad model"""
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

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='TA', verbose_name='Категория')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = CKEditor5Field(verbose_name='Текст', config_name='extends', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def get_absolute_url(self):
        """Getting the absolute URL of the particular Ad detail page"""
        return reverse('ad_detail', args=[str(self.id)])


class Response(models.Model):
    """Response model"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор отклика')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='responses')
    text = models.TextField(verbose_name='Текст')
    status = models.BooleanField(default=False, verbose_name='Статус')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата отклика')

    def __str__(self):
        return f'{self.author}: {self.text}'

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'


class Subscription(models.Model):
    """Subscription model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
