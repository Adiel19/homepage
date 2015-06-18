from django.db import models

class entry(models.Model):
    name = models.CharField(max_length=45)
    text = models.TextField()
