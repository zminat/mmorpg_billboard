from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse

from accounts.models import UserVerification
from mmorpg import settings


@receiver(post_save, sender=UserVerification)
def send_mail_on_user(sender, instance, created, **kwargs):
    if created:
        subject = 'Код подтверждения регистрации'
        text = f'{instance.user.username}, закончите регистрацию на сайте.'
        verification_link = f'{settings.SITE_URL}{reverse("verification", kwargs={"link_uuid": instance.link_uuid})}'
        html = (
            f'Вы получили это сообщение, потому что пользователь <b>{instance.user.username}</b>, '
            f'указал этот email при регистрации на сайте <a href="{settings.SITE_URL}">Доска объявлений MMORPG</a>. '
            f'Для подтверждения регистрации пройдите по <a href="{verification_link}">ссылке</a> и введите код '
            f'регистрации: {instance.code}'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[instance.user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()
