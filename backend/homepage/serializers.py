from rest_framework import serializers
from .models import postcard, subscribers


class postcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = postcard
        fields = ('id', 'heading', 'image', 'alt', 'text', 'created_at')


class subscribersSerialize(serializers.ModelSerializer):
    class Meta:
        model = subscribers
        fields = ('id', 'email')
