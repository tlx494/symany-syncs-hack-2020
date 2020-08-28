import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

df = pd.read_csv("clickbait_data.csv", header=0)

X = df['headline']
y = df['clickbait']

count_vect = CountVectorizer()

X_train_counts = count_vect.fit_transform(X)

tfidf_transformer = TfidfTransformer()

X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
#clf = MultinomialNB().fit(X_train_tfidf, y)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB())
])

text_clf.fit(X, y)
test_eg = ['Coronavirus: NSW records 13 new cases of COVID-19', 'Try this out and see what happens!', 'The personality cult Donald Trump launched in 2016 has subsumed the Republican Party', 'The University of Paris-Saclay has a teaching and research staff of 9,000, catering to 48,000 students—more than Harvard or Stanford', 'Bulgarians have been Europe’s gardeners longer than you think']

# X_new_counts = count_vect.transform(test_eg)
# X_new_tfidf = tfidf_transformer.transform(X_new_counts)

prediction = text_clf.predict(test_eg)
print(prediction)
#scores = cross_val_score(text_clf, X, y, cv=10)
#print(scores)
#print(text_clf.score(X_test, y_test))

# for p in prediction:
#     if p:
#         print("Clickbait")
#     else:
#         print("Not clickbait")

#print(prediction)