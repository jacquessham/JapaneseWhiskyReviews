# Japanese Whisky Reviews

There is a Japanese Whisky Review data set available in Kaggle, that the data set is  originated from Master of Malt. I am interested in doing some NLP works on this data set. <br><br>
I will be making some analysis on the sentiment of the reviews and try to summarize the individual review.
<br><br>
<b>The current version is 2.0.</b> You may find the previous versions in the [Archive](/Archive) folder.

## Tools
In this project, I will be using packages like SKlearn, vaderSentiment, ntlk for sentiment scores and TF-IDF. Then, we will display the result on a dashboard via Plotly Dash.

## Data set
The data set could be found in <a href="https://www.kaggle.com/koki25ando/japanese-whisky-review">Kaggle</a>. It consists of 4 columns including, bottle label, brand name, title of the review and the review content. The data set only covers 4 Japanese whisky brands -- Yamazaki, Hibiki, Hakushu, and Nikka.


## Dashboard
The dashboard consists of two parts: <b>Sentiment Analysis</b> and <b>TF-IDF Analysis</b> (Core meaning of a posted comment). The Sentiment Analysis is plotted with a static box plot of sentiment scores distribution by whiksy brand. The bottom has 4 tabs represent each whisky brand. You may click on one whisky and the dashboard would randomly pick a comment and display the core meaning.
<br><br>
The dashboard looks like this:

<img src=jp_whisky_dashboard.png>

### How to Run the Dashboard?
After ensuring installing all the dependencies, you run simply execute:

```
python viz.py
```

Once the dashboard is ready, you may access it at <b>127.0.0.1:9000</b>

## Technical Explanation
### Sentiment Analysis
We will use vaderSentiment to calculate the sentiment score for each review. Then, Plotly will visualize the range of sentiment score of each brand with a boxplot and render on the Dashboard. It looks like this. <br><br>
<img src=jp_whisky_boxplot.png>
<br>
From the boxplot, we can learn that reviewers in general have a positive view on the Japanese whiskies, while they have better impression on Nikka and Hibiki. Interestingly, the median sentiment score on Yamazaki is 0, which means neutral.

### TF-IDF Analysis
The second task is to build a model that shows the summary by displaying the top 5 key words in the review. The script uses TfidfVectorizer from sklearn.feature_extraction.text to build the model. To preprocess the texts, I used the same package to remove English stop words and nltk to stem the words.
<br>
<a href="jpwhisky_review_tfidf.py">jpwhisky_review_tfidf.py</a> is the backend, and the Dashboard <a href="">viz.py</a> will provoke the implementation and display result.

## Files
Here are the files to run the dashboards:

### viz.py
The driver file to construct the dashboard and backend.

### jpwhisky_review_sentiment.py
The helper script to calculate sentiment scores in the backend.

### jpwhisky_reivew_tfidf.py
The helper script to calculate TF-IDF scores in the backend.

### viz_helper Folder
The framework to render a Plotly visualization, the blueprint comes from the <a href="https://github.com/jacquessham/DashExamples/tree/master/PlotlyTemplateFramework">DashExamples Respository</a> with some modification.
