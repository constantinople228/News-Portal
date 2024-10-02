from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import datetime

from django.dispatch import receiver
from news.models import Post, Category
from django.db.models.signals import m2m_changed
from django.template.loader import render_to_string
from .models import PostCategory


@shared_task
def send_notifications(preview, pk, heading, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=heading,
        body='',
        from_email='kostyaslobodskoi@yandex.ru',
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

    @receiver(m2m_changed, sender=PostCategory)
    def notify_about_new_post(sender, instance, **kwargs):
        if kwargs['action'] == 'post_add':
            categories = instance.category.all()
            subscribers_emails = []

            for cat in categories:
                subscribers = cat.subscribers.all()
                subscribers_emails += [s.email for s in subscribers]

            send_notifications(instance.preview(), instance.pk, instance.heading, subscribers_emails)


@shared_task()
def weekly_send_email():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_create__gte=last_week)
    categories = set(posts.values_list('category__name_category', flat=True))
    subscribers = set(
        Category.objects.filter(name_category__in=categories).values_list('subscribers__email', flat=True))

    html_content = render_to_string(
        'weekly_news.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Новые статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

