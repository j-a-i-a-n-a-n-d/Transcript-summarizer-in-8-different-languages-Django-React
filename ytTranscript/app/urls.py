"""
URL configuration for ytTranscript project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello'),
    path('getLanguages/', GetLanguagesView.as_view(), name='getLanguages'),
    path('getSummary/', GetSummaryView.as_view(), name='getSummary'),
    path('tfidfSummary/', TFIDFSummaryView.as_view(), name='tfidfSummary'),
    path('getData/', TranscriptsSummaryListView.as_view(),
         name='TranscriptsSummaryListView'),
    path('getData/<str:url>/', TranscriptsSummaryListView.as_view(),
         name='TranscriptsSummaryDetailView'),
]
