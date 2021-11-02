from django.db import models

# Create your models here.
class APIData(models.Model):
    start=models.CharField(max_length=200)
    dur=models.CharField(max_length=200)
    timeleft=models.CharField(max_length=200)
    event=models.CharField(max_length=200)

