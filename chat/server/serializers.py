from rest_framework import serializers
from .models import Category, Server


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = "__all__"
