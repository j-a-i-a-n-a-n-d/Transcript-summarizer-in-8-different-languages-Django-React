from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline


def get_summary(transcript):
    summariser = pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6",
        tokenizer="sshleifer/distilbart-cnn-12-6",
        revision="a4f8f3e",
    )

    summary = ''
    for i in range(0, (len(transcript)//500)+1):
        summary_text = summariser(
            transcript[i*500:(i+1)*500])[0]['summary_text']
        summary = summary + summary_text + ' '
    return summary


def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript


def list_languages(video_id):
    lanuages = YouTubeTranscriptApi.list_transcripts(video_id)
    return lanuages


def get_language_code(text):
    return text.split()[0]


def get_language_name(text):
    return text.split()[1].split('[')[0]


def languageFilter(word):
    return word.strip('(').strip(')').strip('"')


def get_trancriptsX(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(
        video_id, languages=['hi'])
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript


youtube_link = "https://www.youtube.com/watch?v=74ijsBhbxSQ"
youtube_link = youtube_link.split('=')[1]
# transcripts = get_transcript(youtube_link)
languages = list_languages(youtube_link)
trancriptsX = get_trancriptsX(youtube_link)
# print(trancriptsX)
summary = get_summary(trancriptsX)
print(summary)
# print((languages))
# print(transcripts)
for l in languages:
    print(get_language_code(str(l)), " ",
          languageFilter(get_language_name(str(l))))
