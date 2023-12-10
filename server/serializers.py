from rest_framework import serializers
from server.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['bookId', 'title', 'author', 'edition', 'publisher', 'language', 'publicationDate', 'numberOfCopies']

    read_only_fields = ['bookId']

    def create(self, validated_data):
        return Book.objects.create(**validated_data)