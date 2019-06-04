from rest_framework import serializers
from rolepermissions.roles import assign_role
from rest_framework.serializers import StringRelatedField

from .models import *


class UserSerializer(serializers.ModelSerializer):
    # books = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')  # , 'books'
        extra_kwargs = {'password': {'write_only': True}}
        # default_permissions=()

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        assign_role(user, 'doctor')
        user.save()
        return user


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'books')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
