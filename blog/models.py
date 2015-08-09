from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateField('date published')
