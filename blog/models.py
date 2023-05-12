from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=155)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, related_name='books', on_delete=models.CASCADE)
    date_published = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(datetime.now().year)])
    publishing_house = models.CharField(max_length=255)
    number_of_pages = models.IntegerField(validators=[MinValueValidator(1)])
    cover = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    def __str__(self):
        return self.name
