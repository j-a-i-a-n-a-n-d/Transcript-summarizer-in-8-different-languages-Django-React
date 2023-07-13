from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline


def list_languages(video_id) -> object:
    try:
        languages = YouTubeTranscriptApi.list_transcripts(video_id)
        return languages
    except Exception as e:
        raise ValueError(
            "Invalid YouTube video ID or unable to retrieve transcripts.") from e


def get_language_code(text) -> str:
    return text.split()[0]


def get_language_name(text) -> str:
    return text.split()[1].split('[')[0]


def languageFilter(word) -> str:
    return word.strip('(').strip(')').strip('"')


def get_trancriptsX(video_id, language) -> str:
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(
            video_id, languages=[language])
        transcript = ' '.join([d['text'] for d in transcript_list])
        return transcript
    except Exception as e:
        raise ValueError(
            "Invalid YouTube video ID or unable to retrieve transcripts.") from e


def get_summary(transcript) -> str:
    try:
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
    except Exception as e:
        raise ValueError(
            "Invalid YouTube video ID or unable to retrieve transcripts.") from e
