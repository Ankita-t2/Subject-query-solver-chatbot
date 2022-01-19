import  nltk
# nltk.download('punkt')
import numpy as np
from nltk.stem.porter import PorterStemmer
stemmer=PorterStemmer()
def tokenize(sentence):
    return nltk.wordpunct_tokenize(sentence)
def stem(word):
    return stemmer.stem(word.lower())
def bag_of_words(tokenized_sentense,all_words):
    tokenized_sentense=[stem(w) for w in tokenized_sentense]
    bag=np.zeros(len(all_words),dtype=np.float32)
    for idx,w in enumerate(all_words):
        if w in tokenized_sentense:
            bag[idx]=1.0
    return bag
# sentence=["hello",  "how","are", "you"]
# words=["hi","hello","i","you","bye","thank","cool"]
# bag=bag_of_words(sentence,words)
# print(bag)



# a="How are you ?"
# print(a)
# a=tokenize(a)
# print(a)
# words=["index","indexing","indexed"]
# stem_word=[stem(w) for w in words]
# print(stem_word)