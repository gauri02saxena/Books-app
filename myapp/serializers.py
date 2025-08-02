from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book
from .models import Author

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    """
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    """
    class Meta:
        model = Author
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    """
    Handles user registration.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
