from rest_framework import serializers
from book_api.models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    page_number = serializers.IntegerField()
    publish_data = serializers.DateField()
    stock = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.page_number = validated_data.get("title", instance.page_number)
        instance.publish_data = validated_data.get("title", instance.publish_data)
        instance.stock = validated_data.get("title", instance.stock)
        instance.save()
        return instance

