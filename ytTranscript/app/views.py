from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .yt_summarizer import *
from .yt_tfidf import *


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


class TFIDFSummaryView(APIView):
    def post(self, request):
        try:
            youtube_link = request.data.get('youtube_link')
            youtube_link = youtube_link.split('=')[1]
            transcripts = get_trancriptsX(youtube_link, "en")
            sentences = clean_text(transcripts)
            text_data = cnt_in_sent(sentences)
            freq_list = freq_dict(sentences)
            tf_scores = calc_TF(text_data, freq_list)
            idf_scores = calc_IDF(text_data, freq_list)
            tfidf_scores = calc_TF_IDF(tf_scores, idf_scores)
            sent_data = sent_scores(tfidf_scores, sentences, text_data)
            result = summary(sent_data)
            return Response({"summary": result}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Response": "Invalid YouTube video ID or unable to retrieve transcripts."}, status=status.HTTP_400_BAD_REQUEST)
