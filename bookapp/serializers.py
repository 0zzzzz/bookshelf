from rest_framework import serializers
from .models import Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def create(self, validated_data):
        return Books.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.name = validated_data.get('name ', instance.name)
        instance.text = validated_data.get('text', instance.text)
        instance.short_desc = validated_data.get('short_desc', instance.short_desc)
        instance.save()
        return instance
