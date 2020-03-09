from django.contrib.auth import admin
from django.db import models
from django.conf import settings
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200, default='')
    prev = models.TextField(blank=True, max_length=200, default='')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def create_preview(self):
        if self.prev == '':
            self.prev = self.text[:100] + '...'

    def __str__(self):
        return self.title
