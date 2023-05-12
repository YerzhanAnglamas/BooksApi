from rest_framework import serializers
from .models import Author, Genre, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname', 'date_of_birth', 'date_of_death']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'genre', 'date_published', 'publishing_house', 'number_of_pages', 'cover']


class GetBookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'genre', 'date_published', 'publishing_house', 'number_of_pages', 'cover']
