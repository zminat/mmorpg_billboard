from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse
from billboard.models import Response


@receiver(post_save, sender=Response)
def send_mail_on_response(sender, instance, created, **kwargs):
    """
    Sends emails about a new response to the authors of the Ad and the responder.
    :param sender: The Response model class that triggered this signal.
    :param instance: The actual instance of the Response model that was saved.
    :param created: A boolean indicating whether a new instance was created (True) or an existing instance was updated (False).
    :param kwargs: Additional keyword arguments passed to the signal handler.
    :return: None
    """
    responder = instance.author
    ad = instance.ad
    if created:
        subject = 'Получен новый отклик!'
        text = f'{ad.author.username}, кто-то откликнулся на Ваше объявление'
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[ad.author.email]
        )
        responses_link = reverse('responses')
        html = (
            f'<b>{responder.username}</b> откликнулся на объявление "{ad.title}".'
            f'Принять или отклонить отклик Вы можете по <a href="{responses_link}">ссылке</a>.'
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        subject = 'Отклик отправлен!'
        text = (f'{responder.username}, Вы оставили отклик на объявление "{ad.title}". '
                      f'Когда автор объявления примет решение, Вы получите письмо о статусе отклика.')
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[responder.email]
        )
        msg.send()

    if instance.status:
        subject = 'Отклик принят!'
        text = f'Поздравляем! Ваш отклик на объявление "{ad.title}" был принят!'
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[responder.email]
        )
        msg.send()
