from random import randint
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from jpwhisky_review_tfidf import *
from jpwhisky_review_sentiment import *


##### Data and Predictions #####
# This is hardcode because the dataset is always static
filename = 'japanese_whisky_review.csv' 
colname = 'Review_Content'
whiskies = ['Hibiki', 'Yamazaki', 'Hakushu','Nikka']
df, comments_list = read_reviews(filename, colname)

article_index = randint(0, df.shape[0])
top_n = 5
features, scores = tfidf_fit_trans(comments_list)
result_features, result_scores = get_results(features, scores,
                                             article_index, top_n)


##### Dashboard layout #####
# Dash Set up
app = dash.Dash()

# Base Layout
app.layout = html.Div([
	html.Div(), # BoxPlot
	dcc.Tabs(id='whisky-tabs', value='' ,children=[
		dcc.Tab(), # Tab 1, End whisky1-tab
		dcc.Tab(), # Tab 2, End whisky2-tab
		dcc.Tab(), # Tab 3, End whisky3-tab
		dcc.Tab() # Tab 4, End whisky4-tab
		]) # End Tabs
	]) # End base Div

if __name__ == '__main__':
    app.run_server(debug=True, port=9000)