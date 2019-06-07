import re
import string
import pandas as pd
import numpy as np
from nltk.stem.porter import *
from sklearn.feature_extraction import stop_words
from sklearn.feature_extraction.text import TfidfVectorizer


# Define tokenizer for Tfidf model
def tokenizer(post):
    regex = re.compile('[' + re.escape(string.punctuation) + ' 0-9\\r\\t\\n]')
    stemmer = PorterStemmer()
    sentence = regex.sub(' ', post.lower())
    temp_list = sentence.split(' ')
    temp_list = [stemmer.stem(word) for word in temp_list if 
                 word != '' and word not in stop_words.ENGLISH_STOP_WORDS]
    return temp_list

# Read file and extract the comments and convert to np array
def read_reviews(filename, colname):
    jp_whisky = pd.read_csv(filename)
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
