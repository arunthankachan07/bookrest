from django.db import models

# Create your models here.
from rest_framework.serializers import ModelSerializer


class Book(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=100)
    pages=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return self.book_name





