from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255,unique=True)
    description=models.TextField("book description")
    rate=models.PositiveSmallIntegerField(default=0)
    views=models.PositiveIntegerField(default=0)
