from django.db import models
from django.utils import timezone

# Create your models here.

class Person(models.Model) :
    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(default='자기소개', max_length=200)
    age = models.IntegerField(default=0)
    major = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)
    hometown = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self) :
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
