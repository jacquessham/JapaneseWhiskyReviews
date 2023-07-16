FROM python:3.7.1

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN pip uninstall --yes werkzeug
RUN pip install -v https://github.com/pallets/werkzeug/archive/refs/tags/2.0.3.tar.gz

ADD ./viz_helper /code/viz_helper
COPY viz.py /code/viz.py
COPY jpwhisky_review_sentiment.py /code/jpwhisky_review_sentiment.py
COPY jpwhisky_review_tfidf.py /code/jpwhisky_review_tfidf.py

COPY japanese_whisky_review.csv /code/japanese_whisky_review.csv

CMD ["python","viz.py"]
