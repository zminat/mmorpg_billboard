from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User


@receiver(pre_save, sender=User)
def my_handler(sender, instance, created, **kwargs):
    mail = instance.article.author.email
    send_mail(
        'Subject here'
        'Here is the message'
        'host@mail.ru',
        [mail],
        fail_silently=False,
    )