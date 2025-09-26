from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Expense
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
        )
        return user

    def to_representation(self, instance):
        """Customize response to include JWT tokens"""
        data = super().to_representation(instance)
        refresh = RefreshToken.for_user(instance)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ExpenseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Expense
        fields = ['id', 'user', 'category', 'amount', 'date', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']
