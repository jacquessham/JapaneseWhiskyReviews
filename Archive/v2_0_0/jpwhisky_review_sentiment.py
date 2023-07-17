import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Calculate sentiment score on one element
def get_score(x):
	judge = SentimentIntensityAnalyzer()
	return judge.polarity_scores(x)['compound']

# Calculate sentiment score on a pandas dataframe
def calculate_sentiment_scores(df):
	df['score'] = df.apply(lambda x: get_score(x['Review_Content']), axis=1)
	return df
