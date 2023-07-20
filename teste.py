import json
import random

import nltk
import numpy
import requests
from nltk.stem import SnowballStemmer
from nltk.corpus import machado
import pickle

from keras.models import load_model

STEMMER = SnowballStemmer("portuguese")

IGNORE_LETTERS = [".", ';', '/', '?', '!', '"\"', ",", "...", "-", "(", ")", "_", "'", "_", "[", "]", "{", "}", "¡!"]

intents = requests.get("http://127.0.0.1:8000/json/").json()
print(intents)
intents = intents[0]['intents']

classes = pickle.load(open("classes.pkl", "rb"))

words = pickle.load(open("words.pkl", "rb"))

model = load_model('chatbot_model.h5')
print(words)


def tokenize(sentence):
    tokenized_sentence = nltk.word_tokenize(sentence)
    return tokenized_sentence


def stem(sentence):
    tokenized_sentence = tokenize(sentence)
    stemmed_words = [STEMMER.stem(w.lower()) for w in tokenized_sentence if w not in IGNORE_LETTERS]
    return stemmed_words


words = [STEMMER.stem(word) for word in words if word not in IGNORE_LETTERS]


def bow(sentence, words):
    sentence_words = stem(sentence)
    bag = [0] * len(words)
    verify = False
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1

    bag = numpy.array(bag)
    for i in bag:
        if i == 1:
            verify = True
        else:
            pass

    if verify:
        print("input aceito")
        return numpy.array(bag)

    else:
        print("input invalido")


def predict_class(sentence):
    bag_of_words = bow(sentence, words)
    res = model.predict(numpy.array([bag_of_words]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        if r[1] > ERROR_THRESHOLD:
            return_list.append({"intents": classes[r[0]], 'probability': str(r[1])})

    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intents']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            print(str(result))
            myobj = {'resposta': str(result)}
            req = requests.post('http://127.0.0.1:8000/respostas/', data={'resposta': str(result)})
            print(req.status_code)
            break
    return result


while True:
    massage = input("mande uma mensagem para luiza:")

    try:
        ints = predict_class(massage)
    except ValueError:
        print("deu ruim")

    res = get_response(ints, intents)
    print("Luiza:" + res)
