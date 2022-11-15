from celery import shared_task

from .models import Post


@shared_task(name="reset_trending_field")
def func(*args, **kwargs):
  Post.objects.update(
    trending=0
  )

  print('trending field has bean reset')
