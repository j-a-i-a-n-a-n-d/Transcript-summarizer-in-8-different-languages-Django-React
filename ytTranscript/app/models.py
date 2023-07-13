from django.db import models

# Create your models here.


class YoutubeModel(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=1000)
    summary = models.TextField()
    lang = models.CharField(max_length=100)
    transcripts = models.TextField()

    def __str__(self):
        return self.url
