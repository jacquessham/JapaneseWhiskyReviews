import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def get_score(x):
	judge = SentimentIntensityAnalyzer()
	return judge.polarity_scores(x)['compound']


jp_whisky = pd.read_csv('japanese_whisky_review.csv')
score = get_score(jp_whisky.iloc[1,3])
print(score)
jp_whisky['score'] = jp_whisky.apply(lambda x: get_score(x[3]), axis=1)
print(jp_whisky)