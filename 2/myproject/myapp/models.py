from django.db import models

class Event(models.Model):
    type = models.CharField(max_length=50)
    path = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.JSONField()

    def __str__(self):
        return f"{self.type} on {self.path} at {self.timestamp}"
