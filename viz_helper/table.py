import dash_html_components as html
from jpwhisky_review_tfidf import get_words


def generate_table_html(result_features, result_scores):
	content = [
		html.Tr([html.Td(html.B('Key Phase')), 
			html.Td(html.B('TF-IDF Score'))])
	]

	for stemword, score in zip(result_features, result_scores):
		# stemword2word = get_words(stemword)
		# word = stemword2word[stemword]
		word = stemword # Delete when stemword2word is ready
		content.append(
			html.Tr([
				html.Td(word),
				html.Td(str(round(score,4)))
				])
			)
	return html.Table(content, style={'width': '90%', 'margin': 'auto', 'text-align': 'center'})
