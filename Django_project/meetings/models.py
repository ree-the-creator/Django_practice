from django.db import models


class Meeting(models.Model):
    title = models.Charfield(max_length=200)
    date = models.DateField()

