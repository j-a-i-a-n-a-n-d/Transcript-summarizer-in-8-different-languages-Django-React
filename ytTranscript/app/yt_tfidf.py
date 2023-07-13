import re
import nltk
import math
from nltk.tokenize import word_tokenize
from deepmultilingualpunctuation import PunctuationModel
model = PunctuationModel()


# converting the input block to a list of sentences along with cleaning the text
def clean_text(filedata) -> list:
    filedata = model.restore_punctuation(filedata)
    article = filedata.split(". ")
    sentences = []
    for sentence in article:
        sentence = re.sub('[^a-zA-Z]', ' ', str(sentence))
        sentence = re.sub('[\s+]', ' ', sentence)
        sentences.append(sentence)
    sentences.pop()
    display = " ".join(sentences)
    print('\n')
    return sentences


def count_words(text) -> int:   # counting the number of words in each sentence
    count = 0
    words = word_tokenize(text)
    for word in words:
        count += 1
    return count


# build dict of the form
# {'id': 1, 'word count': 12}
def cnt_in_sent(s) -> list:
    txt_data = []
    i = 0
    for sent in s:
        i += 1
        count = count_words(sent)
        temp = {'id': i, 'word count': count}
        txt_data.append(temp)
    return txt_data


# building the frequency dictionary of the form
# {'id': 1, 'freq_dict': {'lorem': 1, 'ipsum': 1, 'is': 1, 'simply': 1, 'dummy': 1, 'text': 1, 'of': 1, 'the': 1, 'printing': 1, 'and': 1, 'typesetting': 1, 'industry': 1}
def freq_dict(sentences) -> list:
    i = 0
    freq_list = list()
    for sent in sentences:
        i += 1
        freq_dict = {}
        words = word_tokenize(sent)
        for word in words:
            word = word.lower()
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
            temp = {'id': i, 'freq_dict': freq_dict}
        freq_list.append(temp)
    return freq_list


def calc_TF(text_data, freq_list):  # calculating the TF score of each word in each sentence
    # {'id': 1, 'tf_score': 0.08333333333333333, 'key': 'lorem'}, {'id': 1, 'tf_score': 0.08333333333333333, 'key': 'ipsum'}
    tf_scores = []
    for item in freq_list:
        ID = item['id']
        for k in item['freq_dict']:
            temp = {
                'id': item['id'],
                'tf_score': item['freq_dict'][k]/text_data[ID-1]['word count'],
                'key': k
            }
            tf_scores.append(temp)
    return tf_scores


# calculating the IDF score of each word in each sentence
# {'id': 1, 'idf_score': 0.0, 'key': 'lorem'}
def calc_IDF(text_data, freq_list) -> list:
    idf_scores = []
    cnt = 0
    for item in freq_list:
        cnt += 1
        for k in item['freq_dict']:
            val = sum([k in tempDict['freq_dict'] for tempDict in freq_list])
            temp = {
                'id': cnt,
                'idf_score': math.log(len(text_data)/(val+1)),
                'key': k
            }
            idf_scores.append(temp)
    return idf_scores


# calculating the TF-IDF score of each word in each sentence
# {'id': 1, 'tfidf_score': 0.0, 'key': 'lorem'}
def calc_TF_IDF(tf_scores, idf_scores) -> list:
    tfidf_scores = []
    for j in idf_scores:
        for i in tf_scores:
            if j['key'] == i['key'] and j['id'] == i['id']:
                temp = {
                    'id': j['id'],
                    'tfidf_score': j['idf_score']*i['tf_score'],
                    'key': j['key']
                }
                tfidf_scores.append(temp)
    return tfidf_scores


def sent_scores(tfidf_scores, sentences, text_data) -> list:
    sent_data = []
    for txt in text_data:
        score = 0
        for i in range(0, len(tfidf_scores)):
            t_dict = tfidf_scores[i]
            if txt['id'] == t_dict['id']:
                score += t_dict['tfidf_score']
        temp = {
            'id': txt['id'],
            'score': score,
            'sentence': sentences[txt['id']-1]
        }
        sent_data.append(temp)
    return sent_data


def summary(sent_data) -> str:  # Generating the Summary
    cnt = 0
    summary = []
    for t_dict in sent_data:
        cnt = cnt + t_dict['score']
    avg = cnt/len(sent_data)
    for sent in sent_data:
        if sent['score'] >= avg:
            summary.append(sent['sentence'])
    summary = ". ".join(summary)
    return summary
