from django.db import models
from django.db.models.fields import DateTimeField
from django.conf import settings


class Question(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    content = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE, related_name='questions')

    def __str__(self) -> str:
        return self.content


class Answer(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    body = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
        related_name='answers')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL,
        related_name='votes')

    def __str__(self) -> str:
        return self.author.username