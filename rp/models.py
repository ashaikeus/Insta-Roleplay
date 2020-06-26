from django.conf import settings
from django.db import models
from django.utils import timezone

class Message(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=30)
    time_sent = models.DateTimeField(default=timezone.now)


class Fandom(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name    


class Character(models.Model):
    fandom = models.ForeignKey(Fandom, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
