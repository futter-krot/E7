from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Ad(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return str(self.name)


class Tag(models.Model):
    text = models.CharField(max_length=128)
    ad = models.ForeignKey(Ad, related_name="tags", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)


class Comment(models.Model):
    author = models.CharField(max_length=128, default='author')
    text = models.TextField(default='Something...')
    ad = models.ForeignKey(Ad, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ad)

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)


@receiver(post_save, sender=Ad)
@receiver(post_save, sender=Tag)
@receiver(post_save, sender=Comment)
def clear_cache(sender, instance, **kwargs):
    cache.clear()
