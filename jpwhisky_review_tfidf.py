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
jp_whisky = pd.read_csv('japanese_whisky_review.csv')
comments_list = jp_whisky['Review_Content'].tolist()

# Declare model
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
print(result.shape)
index = np.argsort(result.toarray()[1])[::-1]
print(features[index[:5]])
