from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    UID = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 32, unique = True)
    password = models.CharField(max_length = 32)

class Board(models.Model):
    MID = models.AutoField(primary_key = True)
    UID = models.ForeignKey(User, on_delete = models.CASCADE)
    time = models.DateTimeField(default = timezone.now)
    title = models.CharField(max_length = 100)
    message = models.CharField(max_length = 10000)

class Agree(models.Model):
    AID = models.AutoField(primary_key = True)
    MID = models.ForeignKey(Board, on_delete = models.CASCADE)
    UID = models.ForeignKey(User,  on_delete = models.CASCADE)
    agree = models.NullBooleanField()

class Comment(models.Model):
    CID = models.AutoField(primary_key = True)
    MID = models.ForeignKey(Board, on_delete = models.CASCADE)
    UID = models.ForeignKey(User, on_delete = models.CASCADE)
    time = models.DateTimeField(default = timezone.now)
    comment = models.CharField(max_length = 1000)