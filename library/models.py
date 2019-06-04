from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    name = models.CharField(verbose_name='Author', max_length=64)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name='Category', max_length=64)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100, blank=False)
    author = models.ForeignKey('Author', verbose_name='Author', on_delete=models.CASCADE, related_name='books')
    categories = models.ManyToManyField('Category', verbose_name='Categories', related_name='books')
    quantity = models.PositiveIntegerField(verbose_name='Quantity', default=10)
    readers = models.ManyToManyField(User, verbose_name='Readers', blank=True, related_name='books')
    date_pub = models.PositiveSmallIntegerField(verbose_name='Date of publication')

    def __str__(self):
        return self.title
