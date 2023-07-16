import json
from random import choice
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from jpwhisky_review_tfidf import *
from jpwhisky_review_sentiment import *
from viz_helper.generate_plotly import *
from viz_helper.table import *


##### Data and Predictions #####
# This is hardcode because the dataset is always static
filename = 'japanese_whisky_review.csv'
colname = 'Review_Content'
whiskies = ['Hibiki', 'Yamazaki', 'Hakushu', 'Nikka']
df, comments_list = read_reviews(filename, colname)
df.columns = ['index','Bottle_name','Brand','Title','Review_Content']
df['index'] = df['index'].astype(int)

# Calculate Sentiment Scores
df = calculate_sentiment_scores(df)

# Calculate TFIDF scores
features, scores = tfidf_fit_trans(comments_list)

# Prepare Boxplot for sentiment scores
with open('viz_helper/arguements.json') as f:
    args = json.load(f)
fig = generate_plotly_viz(
    df, args['metadata'], args['viz_type'], args['viz_name'])

##### Dashboard layout #####
# Dash Set up
app = dash.Dash()

# Base Layout
app.layout = html.Div([
    html.Div([html.H1('Japanese Whisky Review Analysis')],
             style={'width': '90%', 'margin': 'auto', 'text-align': 'center'}
             ),  # Headline
    html.Div(
        dcc.Graph(
            id='sentiment_boxplot',
            figure=fig
        )
    ),  # BoxPlot
    html.Div([html.H3('Please choose from the following whiskies:')],
             style={'width': '90%', 'margin': 'auto', 'text-align': 'center'}
             ),
    dcc.Tabs(id='whisky-tabs', value=whiskies[0], children=[
        dcc.Tab(
                label=whiskies[0],
                value=whiskies[0]
        ),  # Tab 1, End whisky1-tab
        dcc.Tab(
            label=whiskies[1],
            value=whiskies[1]
        ),  # Tab 2, End whisky2-tab
        dcc.Tab(
            label=whiskies[2],
            value=whiskies[2]
        ),  # Tab 3, End whisky3-tab
        dcc.Tab(
            label=whiskies[3],
            value=whiskies[3]
        )  # Tab 4, End whisky4-tab
    ]),  # End Tabs
    html.Div(id='whisky-table')
])  # End base Div

##### Dashboard Callback Function #####
# For Tab1 Only for now
@app.callback(Output('whisky-table','children'),
    [Input('whisky-tabs','value')])
def render_table(tab):
    # Filter to the brand
    df_temp = df[df['Brand'] == tab]
    article_index = choice(df_temp['index'].tolist())
    top_n = 5
    # Obtain scores for a randomly selected comment
    result_features, result_scores = get_results(features, scores,
                                             article_index, top_n)

    sub_headline = 'This post is about ' + \
                df_temp[df_temp['index']==article_index].iloc[0]['Brand'] + "'s " + \
                df_temp[df_temp['index']==article_index].iloc[0]['Bottle_name']

    # sub_headline = 'Hello world!'
    content = html.Div([
        html.H3(sub_headline),
        generate_table_html(result_features, result_scores)
        ],
        style={'width': '90%', 'margin': 'auto', 'text-align': 'center'})
    return content


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=9000)
