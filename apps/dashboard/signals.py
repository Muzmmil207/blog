from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import PostComment


@receiver(post_save, sender=PostComment)
def new_comment(sender, instance, created, **kwargs):
    if created:
        post =  instance.post
        subject = f"New comment in: {post.title}"
        
        message = render_to_string('apps/dashboard/new-post-comment.html', {
            'name': instance.name,
            'comment': instance.comment,
            'email': instance.email,
            'slug': post.slug,
        })
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [post.author.email],
            fail_silently=False,
        )
