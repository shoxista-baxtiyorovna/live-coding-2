from rest_framework import serializers
from .models import Book


class AuthorBookSerializer()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'genre', 'isbn', 'published_date', 'description', 'language', 'page_count', 'copies_available']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['authors'] = AuthorBookSerializer(instance.authors, many=True)
        return data