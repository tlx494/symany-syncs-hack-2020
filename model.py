import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
df = pd.read_csv("clickbait_data.csv", header=0)

X = df['headline']
y = df['clickbait']

count_vect = CountVectorizer()

X_train_counts = count_vect.fit_transform(X)

tfidf_transformer = TfidfTransformer()

X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)


clf = MultinomialNB().fit(X_train_tfidf, y)
test_eg = ['Coronavirus: NSW records 13 new cases of COVID-19', 'Try this out and see what happens!']

X_new_counts = count_vect.transform(test_eg)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

prediction = clf.predict(X_new_tfidf)
print(prediction)
git s