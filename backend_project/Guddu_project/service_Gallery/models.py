from django.db import models

class Service_Gallery(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField
