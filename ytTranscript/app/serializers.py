from rest_framework import serializers
from .models import YoutubeModel


class YoutubeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeModel
        fields = ['id', 'url', 'summary', 'lang', 'transcripts']
