import re
import string
import pandas as pd
import numpy as np
from nltk.stem.porter import *
from sklearn.feature_extraction import _stop_words
from sklearn.feature_extraction.text import TfidfVectorizer


# Preprocess the comment to remove punctuation and split into a list
def clean_words(post):
    regex = re.compile('[' + re.escape(string.punctuation) + ' 0-9\\r\\t\\n]')
    sentence = regex.sub(' ', post.lower())
    return sentence.split(' ')

# Define tokenizer for Tfidf model
def tokenizer(post):
    temp_list = clean_words(post)
    stemmer = PorterStemmer()
    temp_list = [stemmer.stem(word) for word in temp_list if 
                 word != '' and word not in _stop_words.ENGLISH_STOP_WORDS]
    return temp_list

# Read file and extract the comments and convert to np array
def read_reviews(filename, colname):
    jp_whisky = pd.read_csv(filename, encoding = 'ISO-8859-1')
    comments_list = jp_whisky[colname].tolist()
    return jp_whisky, comments_list

# Declare model
def tfidf_fit_trans(comments_list):
    tfidf = TfidfVectorizer(input='content',
                            analyzer='word',
                            tokenizer=tokenizer,
                            stop_words='english',
                            decode_error='ignore')
    # Fit and transform the model
    scorer = tfidf.fit(comments_list)
    result = scorer.transform(comments_list)
    # Get the top 5 scores from each comment
    features = np.array(scorer.get_feature_names())
    scores = result.toarray()
    return features, scores

def get_results(features, scores, article_index, top_n):
    index = np.argsort(scores[article_index])[::-1]
    return features[index[:top_n]], scores[article_index, index[:top_n]]

def get_words(comment):
    temp_list = clean_words(comment)
    stemmer = PorterStemmer()
    word_dict = {}
    for word in temp_list:
        word_stemmed = stemmer.stem(word)
        if word != '' and word not in _stop_words.ENGLISH_STOP_WORDS \
           and word_stemmed not in word_dict:
           word_dict[word_stemmed] = [word]
        elif word != '' and word not in _stop_words.ENGLISH_STOP_WORDS \
           and word_stemmed in word_dict:
           word_dict[word_stemmed] = word_dict[word_stemmed].append(word)
    return word_dict

