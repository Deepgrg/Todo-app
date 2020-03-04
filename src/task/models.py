from django.db import models


class Task(models.Model):
    topic = models.CharField(max_length = 180)
    description = models.TextField(blank= True , null = True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.topic
