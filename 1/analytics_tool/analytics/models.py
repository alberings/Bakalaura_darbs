from django.db import models

class Click(models.Model):
    tag_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Scroll(models.Model):
    position = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class TimeSpent(models.Model):
    time_spent = models.IntegerField()  # in seconds
    created_at = models.DateTimeField(auto_now_add=True)
