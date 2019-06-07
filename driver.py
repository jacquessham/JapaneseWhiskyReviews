from random import randint
from jpwhisky_review_tfidf import *


df, comments_list = read_reviews('japanese_whisky_review.csv',
                                 'Review_Content')
article_index = randint(0, df.shape[0])
top_n = 5
features, scores = tfidf_fit_trans(comments_list)
result_features, result_scores = get_results(features, scores,
                                             article_index, top_n)

result_script = 'This post is about ' + \
                df.loc[article_index, 'Brand'] + "'s " + \
                df.loc[article_index, 'Bottle_name'] +'\n'
for word, score in zip(result_features, result_scores):
	result_script += 'Key phase: '
	result_script += word
	result_script += '\t\t'
	result_script += 'TF-IDF score: '
	result_script += str(round(score,4))
	result_script +='\n'

print(result_script)