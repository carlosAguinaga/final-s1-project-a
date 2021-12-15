import csv
from package_files.stop import stop_words
from collections import Counter

sentimientos = {
    'alegria': ['feliz', 'alegre', 'contento'],
    'miedo': ['muerte', 'fatal', 'enfermedad']
}

stopWords = stop_words('stopwords.txt')

def remove_stopwords(dictinary: dict):

    with open('2020-04-30 Coronavirus Tweets.CSV') as tweets:
        # with open('temp.CSV') as tweets:
        counter = 0
        tweets_reader = csv.DictReader(tweets)
        texts = []

        for row in tweets_reader:
            text = row['text']
            for txt in text.split(' '):
                texts.append(txt)

        for i in texts:
            if i in stopWords:
                counter += 1

        c = Counter(texts)

        print('stopwords eliminadas',counter)
        print(c.most_common(7))



remove_stopwords(sentimientos)
