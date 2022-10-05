from django.db import models

# Create your models here.

class WordFreq(models.Model):
    name = models.CharField(max_length=200, null=True, unique=True)
    top_items = models.JSONField()


    