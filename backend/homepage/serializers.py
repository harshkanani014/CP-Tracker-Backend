from rest_framework import serializers
from .models import postcard, subscribers


class postcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = postcard
        fields = ('id', 'heading', 'image', 'alt',
                  'text', 'link', 'created_at')
