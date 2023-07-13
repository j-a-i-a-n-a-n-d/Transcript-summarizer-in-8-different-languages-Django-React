from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .yt_summarizer import *


class HelloWorldView(APIView):
    def get(self, request):
        return Response("Hello, World!")


class GetLanguagesView(APIView):
    def post(self, request):
        try:
            youtube_link = request.data.get('youtube_link')
            youtube_link = youtube_link.split('=')[1]
            languages = list_languages(youtube_link)
            response = {}
            for l in languages:
                response[get_language_code(str(l))] = languageFilter(
                    get_language_name(str(l)))
            return Response({"body": response}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Response": "Invalid YouTube video ID or unable to retrieve transcripts."}, status=status.HTTP_400_BAD_REQUEST)


class GetSummaryView(APIView):
    language_support = ["en", "fr", "es", "de", "it", "nl", "pt", "ru"]

    def post(self, request):
        try:
            lang = request.data.get('language')
            youtube_link = request.data.get('youtube_link')
            youtube_link = youtube_link.split('=')[1]
            if lang not in self.language_support:
                lang = "en"
            transcripts = get_trancriptsX(youtube_link, lang)
            summary = get_summary(transcripts)
            return Response({"summary": summary, "transcripts": transcripts}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Response": "Invalid YouTube video ID or unable to retrieve transcripts."}, status=status.HTTP_400_BAD_REQUEST)
