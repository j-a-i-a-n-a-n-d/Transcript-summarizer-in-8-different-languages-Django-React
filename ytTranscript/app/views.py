from rest_framework.views import APIView
from rest_framework.response import Response
from .YTsummarizer import *


class HelloWorldView(APIView):
    def get(self, request):
        return Response("Hello, World!")


class SummarizeView(APIView):
    def post(self, request):
        youtube_link = request.data.get('youtube_link')
        youtube_link = youtube_link.split('=')[1]
        transcripts = get_transcript(youtube_link)
        summary = get_summary(transcripts)
        return Response(summary)
