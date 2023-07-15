# Youtube Transcript Summarizer (Chrome Extension)

A YouTube Transcript Summarizer is a tool that can transcribe a YouTube video and generate 2 different types of summaries based on the transcript content.

- Extractive Summarization
- Abstractive Summarization

The project is build by Python-Django as a backend and React on the Frontend. The project is tested on Python 3.10.

## Documentation

- Youtube Transcript API for fetching transcripts and langs
- Abstractive Summarization with Bert
- Extractive Summarization with TF-IDF
- Punctuation Model used for Punctuation transcripts if not (req in case of TF-IDF)
- Capable of Summarization in 8 languages supported.

## Installation

To run the application locally

- $ `git clone repo url `
- $ `git fetch -r`
- $ `git switch historyFeature` (Main is not Updated)
- $ `cd yt Transcript`
- $ `py -3.10 -m venv ve`
- $ `ve\scripts\activate`
- $ `python install -r requirements.txt`
- Now Make Necessary Migrations in Django
- $ `python manage.py runserver`
  Backend Will be up and Running

To Run the Frontend

- $ `cd chromeextension`
- $ `npm install`
- $ `npm start` --> to start the development server
- $ `npm run build` --> to build it and add build folder to your Chrome Extensions (Enable Developer Options in Chrome)

## API Reference

Find attached the Postman COllections Along with the repository.

Endpoints

- /api/getLanguages/ (POST)
  Sends the language of different transcripts
- /api/getSummary/ (POST)
  Sends summary to the client (abstractive)
- /api/tfidfSummary/ (POST)
  sends extractive summarization summary
- /api/getData/ (GET)
- /api/getData/?url=<url>
  logs in all/one the summary of url along with langauge for abstractive summarization

## Tech Stack

**Client:** React

**Server:** Python-Django(Django REST Framework)

**Other Tools:** NLTK, Pytorch, Tensorflow, Hugging Face-pipelines, DeepMultiLingualPunctuation

## Authors

Jai Anand

## References

- [Youtube Transcript API](https://pypi.org/project/youtube-transcript-api/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [hugging Face](https://huggingface.co/)
- [Article-Medium](https://medium.com/spidernitt/how-to-build-a-text-summarizer-from-scratch-1a68e39558c4)

## Future Scope

- getData/ api is not integrated with the frontend.
- imrpovement of accuracy of extractive summarization.
- apis are slow to respond caching can be done on production.
