from rest_framework import serializers

from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=['id','title','author','date','page']

class AuthorSerializer(serializers.ModelSerializer):
    # bookr = serializers.StringRelatedField(many=True, read_only=True)
    # bookr = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='book-detail') #-detail is compulsory in view_name=
    # bookr = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    bookr = serializers.SlugRelatedField(many=True, read_only=True,slug_field='title')
    class Meta:
        model = Author
        fields=['id','name','gender','bookr']