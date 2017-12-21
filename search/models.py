from django.db import models
from django.utils import timezone

class Person(models.Model):
    person_name = models.CharField(max_length=200)
    person_photo = models.TextField()

    def __str__(self):
        return self.person_name

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
