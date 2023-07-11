from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline


def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript


def get_summary(transcript):
    summariser = pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6",
        tokenizer="sshleifer/distilbart-cnn-12-6",
        revision="a4f8f3e",
        max_length=100,
    )
    summary = ''
    for i in range(0, (len(transcript)//1000)+1):
        summary_text = summariser(
            transcript[i*1000:(i+1)*1000])[0]['summary_text']
        summary = summary + summary_text + ' '
    return summary
